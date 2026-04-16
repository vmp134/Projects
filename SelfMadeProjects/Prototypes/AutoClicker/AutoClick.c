#include <linux/uinput.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    //Setup, with an FD to /dev/uinput and our uinput_setup struct
    int fd = open("/dev/uinput", O_RDONLY);
    struct uinput_setup usetup;

    //Configuring mouse clicks
    ioctl(fd, UI_SET_EVBIT, EV_KEY); 

    //Click
    while(1) {

    }


    //Cleanup
    
    close(fd);
}