import os
import subprocess
import platform
import test


def deleteusb():
    name = subprocess.check_output(["whoami"], text=True).strip()
    paths = f"/run/media/{name}/"

    results = subprocess.check_output(["ls", paths], text=True, cwd="/")
    results = results.split()

    temppath = paths
    for result in results:
        temppath += result

        for file in os.listdir(temppath):
            # deletes only file
            # if os.path.isfile(f"{paths}/{file}"):
            #     os.system(f"rm {paths}/{file}")
            #     print(f"{file} deleted sucessfully!")

            # deletes everything that starts with day
            # os.system(f"ls {paths}")
            if file.startswith("day"):
                os.system(f"rm -rf {temppath}/{file}")
                print(f"{file} deleted sucessfully!")
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
    partation = test.get_usb_partition()
    if partation != None:
        for part in partation:
            data = f"{part}1"
            mount_device(data)
        deleteusb()
