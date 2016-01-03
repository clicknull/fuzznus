# fuzznus 
FuzzNus python based GDB script that there are a lot of features. Recently I was doing research on grub, therefore I wrote it using Python API. FuzzNus allows you to the desired instruction searching in frame pointers (or memory). Then you can use as you want (such as instruction breakpoint,vulnerability instruction etc.)

Usage: </br>
  (gdb) source /home/dmr/fuzznus.py </br>
  (gdb) nus lea
  
Output:</br>
  (gdb) nus lea</br>
  Disasm</br>
  0xe728 === leave  </br>
  Frame name: </br>
  grub_getkey</br>
  Disasm</br>
  0x7fb11d4 === lea    eax,[edi+0x2] </br>
  Frame name: </br>
  None</br>
  Disasm</br>
  0x7fb11de === lea    eax,[edi+0x1] </br>
  Frame name:  </br>
  None</br>
  Disasm</br>
  0x7fb1208 === lea    eax,[ebp-0x818] </br>
  Frame name: </br>
  None</br>
