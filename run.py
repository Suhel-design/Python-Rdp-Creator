# @title Not use Code
import os
import subprocess

username = "user"
password = "root"

print("Creating User and Setting it up")

# Creation of user
os.system(f"useradd -m {username}")

# Add user to sudo group
os.system(f"adduser {username} sudo")

# Set password of user to 'root'
os.system(f"echo '{username}:{password}' | sudo chpasswd")

# Change default shell from sh to bash
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

print(f"User created and configured having username `{username}` and password `{password}`")
#Run in cell 2


print("CRP: Visit http://remotedesktop.google.com/headless and copy the command after Authentication")

CRP = input("Enter your CRP: ")

Pin = input("Enter Pin (more or equal to 6 digits):")

#Run in cell 3
class CRD:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChorme()
        # self.installblender3()
        self.installnvidiadriver()
        self.finish(user)
        print("\nRDP created succesfully move to https://remotedesktop.google.com/access")

    @staticmethod
    def installCRD():
        print("Installing Chrome Remote Desktop")
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installDesktopEnvironment():
        print("Installing Desktop Environment")
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("systemctl disable lightdm.service")

    @staticmethod
    def installGoogleChorme():
        print("Installing Google Chrome")
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installblender3():
        print("Installing blender 3.2.2")
        subprocess.run(["wget", "https://download.blender.org/release/Blender3.2/blender-3.2.2-linux-x64.tar.xz"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', 'xz-utils'], stdout=subprocess.PIPE)
        subprocess.run(['tar', '-xf', '/content/blender-3.2.2-linux-x64.tar.xz'], stdout=subprocess.PIPE)

    @staticmethod
    def installnvidiadriver():
        print("Installing nvidia driver")
        #subprocess.run(['apt', '-get', 'install', 'linux-headers']stdout=subprocess.PIPE)
        #subprocess.run(['distribution','=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e', 's/\.//g')]stdout=subprocess.PIPE)
        subprocess.run(["wget", "https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-keyring_1.0-1_all.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "-i" "cuda-keyring_1.0-1_all.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', '-get', 'update'], stdout=subprocess.PIPE)
        subprocess.run(['apt', '-get', '-y', 'install', 'cuda-drivers'], stdout=subprocess.PIPE)


    @staticmethod
    def finish(user):
        print("Finalizing")
        
        os.system(f"adduser {user} chrome-remote-desktop")
        command = f"{CRP} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")


        print("Finished Succesfully")


try:
    if CRP == "":
        print("Please enter authcode from the given link")
    elif len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRD(username)
except NameError as e:
    print("'username' variable not found, Create a user first")
