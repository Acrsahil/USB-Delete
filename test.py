import os
import subprocess



# os.system("ls")
#
# # print("***************************************")
# # print("***********Your are hacked*************")
# # print("***************************************")
#
#
# os.system("dolphin && exit")
#


def removeint(st):
    ans = ""
    for i in st:
        if not (i > "0" and i < "9"):
            ans += i
    return ans


def get_usb_partition():
    # Run lsblk to get block devices and their types
    result = subprocess.run(
        ["lsblk", "-lno", "NAME,RM,TYPE,MOUNTPOINT"], capture_output=True, text=True
    )

    lines = result.stdout.splitlines()

    # Search for removable disk (RM = 1)
    listofusb = set()
    for line in lines:
        columns = line.split()

        if len(columns) <= 3 and columns[1] == "1":
            data = removeint(columns[0])
            if len(listofusb) > 0:
                listofusb.add(f"{data}")
            elif len(listofusb) == 0:
                listofusb.add(f"{data}")

            # Now find the partitions for this device

    if len(listofusb) < 1:
        return None
    return listofusb  # Assuming it's a single partition USB drive


partation = get_usb_partition()
i = 1
for part in partation:
    data = f"{part}{i}"
    i += 1
