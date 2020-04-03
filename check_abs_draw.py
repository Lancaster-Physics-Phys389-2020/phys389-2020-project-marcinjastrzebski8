from abs_draw_ham import Draw_ham
from abs_draw_shm import Draw_shm
from abs_draw_bob_paths import Draw_bob
from abs_draw_beats import Draw_beats

"""
mydrawing = Draw_ham()
mydrawing.get_dataset('beats_test.csv')
mydrawing.name_axes('Time','Hamiltonian')
mydrawing.draw()
mydrawing.show()

myshm = Draw_shm()
#make period only in first entry
myshm.get_dataset('check_raise.csv')
myshm.name_axes('Time',R'$\theta_{2}$')
myshm.draw()
myshm.show()

mybob = Draw_bob()
#make it look neater, maybe colourmap, also make sure axes are right size
mybob.get_dataset('beats_test.csv')
mybob.name_axes('x','y')
mybob.draw()
mybob.show()
"""
mybeat = Draw_beats()
#at theta = 0.2 there is noticable shift so maybe change restrictions
mybeat.get_dataset('beats_test.csv')
mybeat.name_axes('time',R'$\theta_{1}$')
mybeat.draw()
mybeat.show()

"""DO DRAW ALL BUT ITS NOT URGENT, FOCUS ON
 THE REPORT AND FINAL TOUCHES TO THE ABOVE FIRST"""