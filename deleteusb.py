import os
import subprocess
import platform
import drivePartation


def deleteusb():
    name = subprocess.check_output(["whoami"], text=True).strip()
    paths = f"/run/media/{name}/"

    results = subprocess.check_output(["ls", paths], text=True, cwd="/")
    results = results.split()

    temppath = paths

    user_feedback = input(
        "Are you sure you want to format your usb drive: press y to delete n to cancel: "
    )

    if user_feedback == "y" or user_feedback == "yes":
        # this is the iterative way to delete each file one by one but cannot delete all the file and dir

        # for result in results:
        #     temppath += result
        #     looppath = temppath
        #
        #     for file in os.listdir(temppath):
        #         # Warning !!!! delete everything in usb
        #         # os.system(f"rm -rf {temppath}/{file}")
        #         print(f"{temppath}/{file} deleted sucessfully!")
        #         temppath = looppath
        #     temppath = paths

        # this is the one cmd way to delete all the contents at once it work in every case

        for result in results:
            temppath += result
            os.system(f"rm -rf {temppath}/*")
            print(f"{result} formated sucessfully!")
            temppath = paths


def is_device_mounted(device):
    """Check if the device is already mounted."""
    try:
        # Check the list of mounted devices using the 'mount' command
        result = subprocess.check_output(["mount"], text=True)
        return device in result
    except subprocess.CalledProcessError as e:
        # Handle error in case 'mount' command fails
        print(f"Error checking mounted devices: {e}")
        return False


def mount_device(device):
    """Mount the device only if it isn't mounted."""
    if not is_device_mounted(device):
        print(f"{device} is not mounted, mounting now...")
        print(device)
        os.system(f"udisksctl mount -b /dev/{device}")


current_os = platform.system()


if current_os == "Linux":
    partation = drivePartation.get_usb_partition()
    if partation != None:
        for part in partation:
            data = f"{part}1"
            mount_device(data)
        deleteusb()
