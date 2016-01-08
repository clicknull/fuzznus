import gdb
class FuzzNus (gdb.Command):
	"Fuzznus gdb script for searching given patterns in memory (equality instruction set)."
	def __init__ (self):
		super (FuzzNus,self).__init__ ("nus",gdb.COMMAND_BREAKPOINTS,gdb.COMPLETE_NONE, False)

	def callfr(self,current_frame,addr,arg):
		inst_enc = current_frame.architecture().disassemble(addr)
		while(True):
			inst_enc = current_frame.architecture().disassemble(addr)
			if(inst_enc[0]['asm'].startswith(arg)):
                                print("Disasm")
                                print(hex(inst_enc[0]['addr'])+" === "+inst_enc[0]['asm'])
                                print("Frame name:")
				print(current_frame.name())
			addr+=inst_enc[0]['length']
                        #if INSTRUCTION Pointer reach to return instruction trigging breakpoint
			if(inst_enc[0]['asm'].startswith('ret')):
				break

	def invoke(self, arg, from_tty):
		counter = 0
		current_frame = gdb.newest_frame()
		while current_frame is not None:
			counter +=1
			addr = current_frame.pc()
			if(addr > -1):
				self.callfr(current_frame,addr,arg)
			current_frame = current_frame.older()
		return hex(0xdeadbeef)



FuzzNus()
