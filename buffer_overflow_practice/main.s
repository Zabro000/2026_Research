	.file	"main.c"
	.text
	.def	__main;	.scl	2;	.type	32;	.endef
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	subq	$288, %rsp
	.seh_stackalloc	288
	leaq	128(%rsp), %rbp
	.seh_setframe	%rbp, 128
	.seh_endprologue
	movl	%ecx, 176(%rbp)
	movq	%rdx, 184(%rbp)
	call	__main
	movq	184(%rbp), %rax
	addq	$8, %rax
	movq	(%rax), %rdx
	leaq	-96(%rbp), %rax
	movq	%rax, %rcx
	call	strcpy
	leaq	-96(%rbp), %rax
	movq	%rax, %rcx
	call	puts
	movl	$0, %eax
	addq	$288, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (GNU) 13.4.0"
	.def	strcpy;	.scl	2;	.type	32;	.endef
	.def	puts;	.scl	2;	.type	32;	.endef
