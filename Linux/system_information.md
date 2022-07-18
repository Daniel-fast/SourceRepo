

####### UNAME(1)                                   

NAME
       uname - print system information

SYNOPSIS
       uname [OPTION]...

DESCRIPTION
       Print certain system information.  With no OPTION, same as -s.

       -a, --all
              print all information, in the following order, except omit -p and -i if unknown:

       -s, --kernel-name
              print the kernel name

       -n, --nodename
              print the network node hostname

       -r, --kernel-release
              print the kernel release

       -v, --kernel-version
              print the kernel version

       -m, --machine
              print the machine hardware name

       -p, --processor
              print the processor type (non-portable)

       -i, --hardware-platform
              print the hardware platform (non-portable)

       -o, --operating-system



#####   Logging In via SSH   

ssh [username]@[IP address]



@@@@@@   What Is /etc/shadow?
https://www.makeuseof.com/etc-shadow-file-linux/

https://www.epochconverter.com/



When you create or change a password in Linux, the system hashes and stores it in the shadow file. Any password rules assigned by the administrator, like expiration dates and inactivity periods, will also remain here. The shadow file can then tell authentication protocols whether a user's password is correct, for example, or when it's expired.

sudo cat /etc/shadow

root:!:19115:0:99999:7:::
daemon:*:19115:0:99999:7:::
bin:*:19115:0:99999:7:::
sys:*:19115:0:99999:7:::
sync:*:19115:0:99999:7:::
games:*:19115:0:99999:7:::
man:*:19115:0:99999:7:::
user:$6$9wNw92ZyamrlEUzy$YkflW/un1Ac46a9uMSGzvs9WJ/7p72WmT8icFfNX.nCdRnF1DGTN3lS6Nw22ir3QmGvapwGwQ7tq/2XEM0GIH1:19187:0:99999:7:::
...

MEANING

muo1:$6$IK2...$20a...:18731:0:99999:7:::
It looks cryptic, and indeed, some of it is encrypted text. The string follows a particular construction, however, and houses specific bits of information, delineated by the colon (:) character.


Here's a complete layout of the string:
[username]:[password]:[date of last password change]:[minimum password age]:[maximum password age]:[warning period]:[inactivity period]:[expiration date]:[unused]

Let's take a closer look at each of these fields:

1. Username
Everything that follows in the string is associated with this username.

2. Password
The password field consists of three additional fields, delineated by dollar signs: $id$salt$hash.

id: This defines the encryption algorithm used to encrypt your password. Values may be 1 (MD5), 2a (Blowfish), 2y (Eksblowfish), 5 (SHA-256), or 6 (SHA-512).
salt: This is the salt used in encrypting and authenticating the password.
hash: This is the user's password as it appears after hashing. The shadow file keeps a hashed version of your password so system can check against any attempt to enter your password.

Sometimes the password field contains only an asterisk (*) or exclamation point (!). That means the system has disabled the user's account, or the user must authenticate through means other than a password. This is often the case for system processes (also known as pseudo-users) that you're likely to find in the shadow file as well.

3. Date of Last Password Change
Here you'll find the last time this user changed their password. Note that the system displays the date in Unix time format.

Take a look of how unix works with data
https://www.makeuseof.com/what-is-unix-time-and-when-was-the-unix-epoch/


4. Minimum Password Age
You'll find here the number of days the user must wait after changing their password before changing it again.

If the minimum is not set, the value here will be 0.

5. Maximum Password Age
This defines how long a user can go without changing their password. Frequently changing your password has its benefits, but by default, the value will be set at a generous 99,999 days. That's close to 275 years.

6. Warning Period
This field determines the number of days before a password has reached its maximum age, during which the user will receive reminders to change their password.

7. Inactivity Period
This is the number of days that can pass after the user's password has reached its maximum age before the system disables the account. Think of this as a "grace period" during which the user has a second chance to change their password, even though it's technically expired.

8. Expiration Date
This date is the end of the inactivity period when the system will automatically disable the user's account. Once disabled, the user will be unable to login until an administrator enables it again.

9. Unused
This field currently serves no purpose and is reserved for potential future use.

##### Showing Date

date  +%s
1657796430

date -d "Jan 2 1970" +%s
104400

%%%%%%  INTERESTING 

executing the command 'date  +%s' in the system at 08h20
1657797620

running in Python 'print(time.time())'
1657797634.400335