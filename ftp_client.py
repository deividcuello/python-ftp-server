import paramiko
import tkinter as tk

window = tk.Tk()
window.configure(bg='white')
window.geometry('430x225')  
window.title("Deivid Cuello FTP Client")
ftpClient_lb = tk.Label(text="Deivid Cuello FTP Client", foreground="black",background="white", font=('Helvetica 18 bold'))

ftpClient_lb.grid(row=0, column=0)
hostname = tk.Label(text="Hostname", foreground="black",background="white", font=('Consolas 14'))
hostname_input = tk.Entry(background="gray90", font=('Helvetica 10 bold'))
username = tk.Label(text="Username", foreground="black",background="white", font=('Consolas 14'))
username_input = tk.Entry(background="gray90", font=('Helvetica 10 bold'))
password = tk.Label(text="Password", foreground="black",background="white", font=('Consolas 14'))
password_input = tk.Entry(background="gray90", font=('Helvetica 10 bold'))

hostf = tk.Label(text="Archivo en host", foreground="black",background="white", font=('Consolas 14'))
hostf_input = tk.Entry(background="gray90",font=('Helvetica 10 bold'))

guestf = tk.Label(text="Archivo en guest", foreground="black",background="white", font=('Consolas 14'))
guestf_input = tk.Entry(background="gray90", font=('Helvetica 10 bold'))

hostname.grid(row=1, column=0)
hostname_input.grid(row=1, column=1,ipady=2, ipadx=30)
username.grid(row=2, column=0)
username_input.grid(row=2, column=1,ipady=2, ipadx=30)
password.grid(row=3, column=0)
password_input.grid(row=3, column=1,ipady=2, ipadx=30)
password_input.config(show="*");

hostf.grid(row=4, column=0)
hostf_input.grid(row=4, column=1,ipady=2, ipadx=30)
guestf.grid(row=5, column=0)
guestf_input.grid(row=5, column=1,ipady=2, ipadx=30)

def subir():
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=hostname_input.get(), username=username_input.get(), password=password_input.get(), allow_agent=False, look_for_keys=False)
	sftp = client.open_sftp()
	sftp.put(hostf_input.get() ,guestf_input.get())
	sftp.close()

def descargar():
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=hostname_input.get(), username=username_input.get(), password=password_input.get(), allow_agent=False, look_for_keys=False)
	sftp = client.open_sftp()
	sftp.get(guestf_input.get(), hostf_input.get())
	sftp.close()

descargar = tk.Button(master=window, text="Descargar", command=descargar, foreground="white",background="green", font=('Consolas 15 bold'))
subir = tk.Button(master=window, text="Subir", command=subir, foreground="white",background="green", font=('Consolas 15 bold'))
descargar.grid(row=6, column=0)
subir.grid(row=6, column=1)

window.mainloop()