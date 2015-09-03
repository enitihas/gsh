while
The syntax of the while command is:
while test-commands; do consequent-commands; done

for
The syntax of the for command is:
for name [in words ...]; do commands; done


case word in [ [(] pattern [ | pattern ] ... ) list ;; ] ... esac

if list; then list; [ elif list; then list; ] ... [ else list; ] fi

until list-1; do list-2; done

Redirecting Input

              [n]<word

Redirecting Output

              [n]>word

The exit, logout, break, con‐
       tinue, let, and shift 

dirs [-clpv] [+n] [-n]
              Without  options,  displays  the  list  of currently remembered directories.  The default display is on a single line with directory
              names separated by spaces.  Directories are added to the list with the pushd command; the popd  command  removes  entries  from  the
              list.



enable [-a] [-dnps] [-f filename] [name ...]
              Enable  and disable builtin shell commands.  Disabling a builtin allows a disk command which has the same name as a shell builtin to
              be executed without specifying a full pathname, even though the shell normally searches for builtins before disk commands.  If -n is
              used,  each  name  is disabled; otherwise, names are enabled.

history -s arg [arg ...]
              With no options, display the command history list with line numbers. 


logout


times  Print the accumulated user and system times for the shell and for processes run from the shell.  The return status is 0.






