M82 ;absolute extrusion mode
M201 X500.00 Y500.00 Z100.00 E5000.00 ;Setup machine max acceleration
M203 X500.00 Y500.00 Z50.00 E50.00 ;Setup machine max feedrate
M204 P500.00 R1000.00 T500.00 ;Setup Print/Retract/Travel acceleration
M205 X8.00 Y8.00 Z0.40 E5.00 ;Setup Jerk
M220 S250 ;Reset Feedrate
M221 S100 ;Reset Flowrate
M302 S0 ;Disable cold extrusion safety
G28 ;Home
G92 E0
G1 X0 Y0 Z66.5 F1000      ;raise z above zero point
G1 X35.25 Y224.75 Z66.5  ;go high above block pickup point 
 
G1 X35.25 Y224.75 Z66.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z66.5 ;raise block up to travel height
G1 X98.75 Y85.05000000000001 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z66.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z66.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z66.5 ;raise block up to travel height
G1 X136.85 Y97.75000000000003 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z66.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z66.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z66.5 ;raise block up to travel height
G1 X162.25 Y110.45000000000002 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z66.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z66.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z66.5 ;raise block up to travel height
G1 X73.35 Y110.45000000000002 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z66.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z66.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z66.5 ;raise block up to travel height
G1 X111.45 Y110.45000000000002 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z66.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z66.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z66.5 ;raise block up to travel height
G1 X98.75 Y135.85000000000002 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z66.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z66.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z66.5 ;raise block up to travel height
G1 X136.85 Y135.85000000000002 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z66.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z91.9 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z91.9 ;raise block up to travel height
G1 X98.75 Y85.05000000000001 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z91.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z91.9 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z91.9 ;raise block up to travel height
G1 X149.55 Y97.75000000000003 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z91.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z91.9 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z91.9 ;raise block up to travel height
G1 X73.35 Y110.45000000000002 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z91.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z91.9 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z91.9 ;raise block up to travel height
G1 X124.14999999999999 Y123.15000000000002 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z91.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z91.9 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z91.9 ;raise block up to travel height
G1 X162.25 Y123.15000000000002 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z91.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z91.9 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z91.9 ;raise block up to travel height
G1 X98.75 Y135.85000000000002 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z91.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z117.3 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z117.3 ;raise block up to travel height
G1 X86.05 Y97.75000000000003 ;go to block placement point
G1 Z67.3 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z117.3 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z117.3 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z117.3 ;raise block up to travel height
G1 X124.14999999999999 Y110.45000000000002 ;go to block placement point
G1 Z67.3 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z117.3 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z117.3 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z117.3 ;raise block up to travel height
G1 X73.35 Y123.15000000000002 ;go to block placement point
G1 Z67.3 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z117.3 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z117.3 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z117.3 ;raise block up to travel height
G1 X98.75 Y135.85000000000002 ;go to block placement point
G1 Z67.3 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z117.3 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z142.7 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z142.7 ;raise block up to travel height
G1 X111.45 Y97.75000000000003 ;go to block placement point
G1 Z92.69999999999999 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z142.7 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z142.7 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z142.7 ;raise block up to travel height
G1 X111.45 Y123.15000000000002 ;go to block placement point
G1 Z92.69999999999999 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z142.7 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z142.7 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z142.7 ;raise block up to travel height
G1 X136.85 Y123.15000000000002 ;go to block placement point
G1 Z92.69999999999999 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z142.7 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 Z168.1 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z168.1 ;raise block up to travel height
G1 X124.14999999999999 Y110.45000000000002 ;go to block placement point
G1 Z118.1 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z168.1 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X35.25 Y224.75 ; finish by going back to block pickup corner but stay at final height
