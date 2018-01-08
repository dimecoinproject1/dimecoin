from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:8372")
old_password = raw_input("Enter old wallet passphrase: ")
new_password = raw_input("Enter new wallet passphrase: ")
confirm_password = raw_input("Enter new wallet passphrase again: ")
if new_password == confirm_password:
	access.walletpassphrasechange(pwd, pwd2)
	print "Password changed successfully"
else:
	print "Password doesn't match!!"