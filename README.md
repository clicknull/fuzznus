# fuzznus 
FuzzNus python based GDB script that there are a lot of features. Recently I was doing research on grub, therefore I wrote it using Python API. FuzzNus allows you to the desired instruction searching in frame pointers (or memory). Then you can use as you want (such as instruction breakpoint,vulnerability instruction etc.)

Usage:
  (gdb) source /home/dmr/fuzznus.py
  (gdb) nus lea
  
Output:
  (gdb) nus lea
  Disasm
  0xe728 === leave  
  Frame name:
  grub_getkey
  Disasm
  0x7fb11d4 === lea    eax,[edi+0x2]
  Frame name:
  None
  Disasm
  0x7fb11de === lea    eax,[edi+0x1]
  Frame name:
  None
  Disasm
  0x7fb1208 === lea    eax,[ebp-0x818]
  Frame name:
  None
