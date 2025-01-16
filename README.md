# smsDailyReminder
A script that sends the SMS to remind about task A in day 1 and task B in day 2 repeatedly.<br>In this example, its a reminder to do the jab into left side and then to the right side on the next day.
<br>Scheduling is to be set in your OS task manager(e.g. systemd timers or cron on Linux or Task Manager on Windows).
<br>A script uses Polish <a href="https://www.smsapi.pl">SMSAPI.pl</a> service, but you can adjust it to another(like e.g. Twilio) as well.
<br><br>For SMSAPI, you will have to install the <b>SmsApiPlClient</b> library:
<br><code>python3 -m pip install smsapi-client</code>
## Usage
<code>./smsDailyReminder</code>
<br><br>Do not forget to set the executable rights to the script file<br>
<br><br>Alternatively:<br><br>
<code>python3 smsDailyReminder.py</code>
<br><br><br>The script saves the Left/Right state into the <i>leftRightState.txt</i> created in the script location.
