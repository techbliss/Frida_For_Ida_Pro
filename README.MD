Frida For Ida PRo

This is plugin for ida pro thar uses the Frida api.
Mainly trace functions.

"Your own scripts get injected into black box processes to execute custom debugging logic.
Hook any function, spy on crypto APIs or trace private application code, no source code needed"

Visit site to get a view what it does.
http://www.frida.re/

Howto

install plugin
Copy folders in archive and copy to root ida folder.
should be
../ida_folder/QTApps/Frida/Frida_For_Ida_Pro.py
../plugins/Frida_caller.py


For installing Frida, have either PIP or easy_install installed and make sure they are added to path.
Then Install with  Plugin


Version 1

Works
PID tracing.
PIP install frida.
Easy_Install frida.
Tracinc spesific functions.
trace intire program, and see how and what sub get called (also how many times sub gets called).
TRace intire program auto write text file of trace.

Remember to get pid before lanching tracer functions.

TODO

Have to Use Qprocess to out put trace and debug input to Qtextbox.
Specially dicover can have so many lines its hard to.
Gonna ad a python code editor, that will work in ida also. when i got the time :).
More functions.

Why

Why not.
