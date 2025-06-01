# Define the text as a multi-line string
text = """
1. Advances in chip technology have made it possible to put an entire controller, includ
ing all the bus access logic, on an inexpensive chip. How does that affect the model of
Fig. 1-5?
2. Given the speeds listed in Fig. 5-1, is it possible to scan documents from a scanner and
transmit them over an 802. l lg network at full speed? Defend your answer.
428 INPUT/OUTPUT CHAP. 5
3. Figure 5-3(b) shows one way of having memory-mapped I/0 even in the presence of
separate buses for memory and VO devices, namely, to first try the memory bus and if
that fails try the VO bus. A clever computer science student has thought of an
improvement on this idea: try both in parallel, to speed up the process of accessing VO
devices. What do you think of this idea?
4. Suppose that a system uses DMA for data transfer from disk controller to main memo
ry. Further assume that it takes t 1 nsec on average to acquire the bus and t2 nsec to
transfer one word over the bus (t 1 » t2). After the CPU has programmed the DMA
controller, how long will it take to transfer 1000 words from the disk controller to
main memory, if (a) word-at-a-time mode is used, (b) burst mode is used? Assume
that commanding the disk controller requires acquiring the bus to send one word and
acknowledging a transfer also requires acquiring the bus to send one word.
5. Suppose that a computer can read or write a memory word in 10 nsec. Also suppose
that when an interrupt occurs, all 32 CPU registers, plus the program counter and
PSW are pushed onto the stack. What is the maximum number of interrupts per sec
ond this machine can process?
6. CPU architects know that operating system writers hate imprecise interrupts. One
way to please the OS folks is for the CPU to stop issuing new instructions when an in
terrupt is signaled, but allow all the instructions currently being executed to finis.h,
then force the interrupt. Does this approach have any disadvantages? Explain your
answer.
7. In Fig. 5-9(b), the interrupt is not acknowledged until after the next character has been
output to the printer. Could it have equally well been acknowledged right at the start
of the interrupt service procedure? If so, give one reason for doing it at the end, as in
the text. If not, why not?
8. A computer has a three-stage pipeline as shown in Fig. l-6(a). On each clock cycle,
one new instruction is fetched from memory at the address pointed to by the PC and
put into the pipeline and the PC advanced. Each instruction occupies exactly one
memory word The instructions already in the pipeline are each advanced one stage.
When an interrupt occurs, the current PC is pushed onto the stack, and the PC is set to
the address of the interrupt handler. Then the pipeline is shifted right one stage and the
first instruction of the interrupt handler is fetched into the pipeline. Does this machine
have precise interrupts? Defend your answer.
9. A typical printed page of text contains 50 lines of 80 characters each. Imagine that a
certain printer can print 6 pages per minute and that the time to write a character to the
printer's output register is so short it can be ignored Does it make sense to run this
printer using interrupt-driven VO if each character printed requires an interrupt that
takes 50 J.lsec ali-in to service?
10. Explain how an OS can facilitate installation of a new device without any need for
recompiling the OS.
11. In which of the four l/0 software layers is each of the following done.
(a) Computing the track, sector, and head for a disk read.
(b) Writing commands to the device registers.
CHAP. 5 PROBLEMS
(c) Checking to see if the user is permitted to use the device.
(d) Converting binary integers to ASCII for printing.
429
12. A local area network is used as follows. The user issues a system call to write data
packets to the network. The operating system then copies the data to a kernel buffer.
Then it copies the data to the network controller board. When all the bytes are safely
inside the controller, they are sent over the network at a rate of 10 megabits/sec. The
receiving network controller stores each bit a microsecond after it is sent. When the
last bit arrives, the destination CPU is interrupted, and the kernel copies the newly
arrived packet to a kernel buffer to inspect it. Once it has figured out which user the
packet is for, the kernel copies the data to the user space. If we assume that each in
terrupt and its associated processing takes 1 msec, that packets are 1024 bytes (ignore
the headers), and that copying a byte takes 1 J..lsec, what is the maximum rate at which
one process can pump data to another? Assume that the sender is blocked until the
work is finished at the receiving side and an acknowledgement comes back. For sim
plicity, assume that the time to get the acknowledgement back is so small it can be
ignored.
13. Why are output files for the printer normally spooled on disk before being printed?
14. RAID level 3 is able to correct single-bit errors using only one parity drive. What is
the point of RAID level 2? After all, it also can only correct one error and takes more
drives to do so.
15. A RAID can fail if two or more of its drives crash within a short time interval. Sup
pose that the probability of one drive crashing in a given hour is p. What is the
probability of a k-drive RAID failing in a given hour?
16. Compare RAID level 0 through 5 with respect to read performance, write per
formance, space overhead, and reliability.
17. Why are optical storage devices inherently capable of higher data density than mag
netic storage devices? Note: This problem requires some knowledge of high-school
physics and how magnetic fields are generated.
18. What are the advantages and disadvantages of optical disks versus magnetic disks?
19. If a disk controller writes the bytes it receives from the disk to memory as fast as it
receives them, with no internal buffering, is interleaving conceivably useful? Discuss.
20. If a disk has double interleaving, does it also need cylinder skew in order to avoid
missing data when making a track-to-track seek? Discuss your answer.
21. Consider a magnetic disk consisting of 16 heads and 400 cylinders. This disk is divid
ed into four 100-cylinder zones with the cylinders in different zones containing 160,
200, 240. and 280 sectors, respectively. Assume that each sector contains 512 bytes,
average seek time between adjacent cylinders is 1 msec, and the disk rotates at 7200
RPM. Calculate the (a) disk capacity, (b) optimal track skew, and (c) maximum data
transfer rate.
22. A disk manufacturer has two 5.25-inch disks that each have 10,000 cylinders. The
newer one has double the linear recording density of the older one. Which disk prop
erties are better on the newer drive and which are the same?
430 INPUT/OUTPUT CHAP. 5
23. A computer manufacturer decides to redesign the partition table of a Pentium hard
disk to provide more than four partitions. What are some consequences of this change?
24. Disk requests come in to the disk driver for cylinders 10, 22, 20, 2, 40, 6, and 38, in
that order. A seek takes 6 msec per cylinder moved. How much seek time is needed
for
(a) First-come, first served.
(b) Closest cylinder next.
(c) Elevator algorithm (initially moving upward).
In all cases, the arm is initially at cylinder 20.
25. A slight modification of the elevator algorithm for scheduling disk requests is to al
ways scan in the same direction. In what respect is this modified algorithm better than
the elevator algorithm?
26. In the discussion of stable storage using nonvolatile RAM, the following point was
glossed over. What happens if the stable write completes but a crash occurs before the
operating system can write an invalid block number in the nonvolatile RAM? Does
this race condition ruin the abstraction of stable storage? Explain your answer.
27. In the discussion on stable storage, it was shown that the disk can be recovered to a
consistent state (a write either completes or does not take place at all) if a CPU crash
occurs during a write. Does this property hold if the CPU crashes again during a
recovery procedure. Explain your answer.
28. The clock interrupt handler on a certain computer requires 2 msec (including process
switching overhead) per clock tick. The clock runs at 60 Hz. What fraction of the
CPU is devoted to the clock?
29. A computer uses a programmable clock i n square-wave mode. If a 500 MHz crystal is
used, what should be the value of the holding register to achieve a clock resolution of
(a) a millisecond (a clock tick once every millisecond)?
(b) 100 microseconds?
30. A system simulates multiple clocks by chaining all pending clock requests together as
shown in Fig. 5-34. Suppose the current time is 5000 and there are pending clock re
quests for time 5008, 5012, 5015, 5029, and 5037. Show the values of Clock header,
Current time, and Next signal at times 5000, 5005, and 5013. Suppose a new (pend
ing) signal arrives at time 5017 for 5033. Show the values of Clock header, Current
time and Next signal at time 5023.
31. Many versions of UNIX use an unsigned 32-bit integer to keep track of the time as the
number of seconds since the origin of time. When will these systems wrap around
(year and month)? Do you expect this to actually happen?
32. A bitmap terminal contains 1280 by 960 pixels. To scroll a window, the CPU (or con
troller) must move all the lines of text upward by copying their bits from one part of
the video RAM to another. If a particular window is 60 lines high by 80 characters
wide (5280 characters, total), and a character's box is 8 pixels wide by 16 pixels high,
how long does it take to scroll the whole window at a copying rate of 50 nsec per
byte? If all lines are 80 characters long, what is the equivalent baud rate of the termi-
CHAP. 5 PROBLEMS 431
nal? Putting a character on the screen takes 5 j.lsec. How many lines per second can
be displayed?
33. After receiving a DEL (SIGINT) character, the display driver discards all output cur
rently queued for that display. Why?
34. On the original IDM PC's color display, writing to the video RAM at any time other
than during the CRT beam's vertical retrace caused ugly spots to appear all over the
screen. A screen image is 25 by 80 characters, each of which fits in a box 8 pixels by
8 pixels. Each row of 640 pixels is drawn on a single horizontal scan of the beam,
which takes 63.6 j.lSec, including the horizontal retrace. The screen is redrawn 60
times a second, each of which requires a vertical retrace period to get the beam back
to the top. What fraction of the time is the video RAM available for writing in?
35. The designers of a computer system expected that the mouse could be moved at a
maximum rate of 20 em/sec. If a mickey is 0.1 mm and each mouse message is 3
bytes, what is the maximum data rate of the mouse assuming that each mickey is re
ported separately?
36. The primary additive colors are red, green, and blue, which means that any color can
be constructed from a linear superposition of these colors. Is it possible that someone
could have a color photograph that cannot be represented using full 24-bit color?
37. One way to place a character on a bitmapped screen is to use bitblt from a font table.
Assume that a particular font uses characters that are 16 x 24 pixels in true RGB color.
(a) How much font table space does each character take?
(b) If copying a byte takes I 00 nsec, including overhead, what is the output rate to the
screen in characters/sec?
38. Assuming that it takes 10 nsec to copy a byte, how much time does it take to com
pletely rewrite the screen of an 80 character x 25 line text mode memory-mapped
screen? What about a 1024 x 768 pixel graphics screen with 24-bit color?
39. In Fig. 5-40 there is a class to RegisterClass. In the corresponding X Window code, in
Fig. 5-38, there is no such call or anything like it. Why not?
40. In the text we gave an example of how to draw a rectangle on the screen using the
Windows GDI:
Rectangle(hdc, xleft, ytop, xright, ybottom);
Is there any real need for the first parameter (hdc), and if so, what? After all, the coor
dinates of the rectangle are explicitly specified as parameters.
41. A THINC terminal is used to display a Web page containing an animated cartoon of
size 400 pixels x 160 pixels running at 10 frames/sec. What fraction of a 100-Mbps
Fast Ethernet is consumed by displaying the cartoon?
42. It has been observed that the THINC system works well with a 1-Mbps network in a
test. Are any problems likely in a multiuser situation? Hint: Consider a large number
of users watching a scheduled TV show and the same number of users browsing the
World Wide Web.
432 INPUT/OUTPUT CHAP. 5
43. If a CPU's maximum voltage, V, is cut to VIn, its power consumption drops to 1 In 2 of
its original value and its clock speed drops to lin of its original value. Suppose that a
user is typing at 1 char/sec, but the CPU time required to process each character is 100
msec. What is the optimal value of n and what is the corresponding energy saving in
percent compared to not cutting the voltage? Assume that an idle CPU consumes no
energy at all.
44. A notebook computer is set up to take maximum advantage of power saving features
including shutting down the display and the hard disk after periods of inactivity. A
user sometimes runs UNIX programs in text mode, and at other times uses the X Win
dow System. She is surprised to find that battery life is significantly better when she
uses text-only programs. Why?
45. Write a program that simulates stable storage. Use two large fixed-length files on your
disk to simulate the two disks.
46. Write a program to implement the three disk-arm scheduling algorithms. Write a driv
er program that generates a sequence of cylinder numbers (0-999) at random, runs the
three algorithms for this sequence and prints out the total distance (number of cylin
ders) the arm needs to traverse in the three algorithms.
47. Write a program to implement multiple timers using a single clock. Input for this pro
gram consists of a sequence of four types of commands (S <int>, T, E <int>, P): S
<int> sets the current time to <int>; T is a clock tick; and E <int> schedules a signal to
occur at time <int>; P prints out the values of Current time, Next signal, and Clock
header. Your program should also print out a statement whenever it is time to raise a
signal.
"""

# Convert text into a list of lines
lines = text.strip().split("\n")

# List of question numbers to extract
question_numbers = [2, 9, 21, 24, 29, 31, 35]

# Extract specific questions based on question numbers
extracted_questions = []
for question_num in question_numbers:
    # Adjust for zero-based indexing (e.g., question 2 is at index 1)
    line_index = question_num - 1
    if line_index < len(lines):
        extracted_questions.append(lines[line_index])

# Print the extracted questions
for question in extracted_questions:
    print(question)
