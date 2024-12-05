M82 ;absolute extrusion mode
M201 X500.00 Y500.00 Z100.00 E5000.00 ;Setup machine max acceleration
M203 X500.00 Y500.00 Z10.00 E50.00 ;Setup machine max feedrate
M204 P500.00 R1000.00 T500.00 ;Setup Print/Retract/Travel acceleration
M205 X8.00 Y8.00 Z0.40 E5.00 ;Setup Jerk
M220 S100 ;Reset Feedrate
M221 S100 ;Reset Flowrate
M302 S0 ;Disable cold extrusion safety
G28 ;Home
G92 E0
G1 X0 Y0 Z46.5 F1000      ;raise z above zero point
G1 X34.5 Y224 Z46.5  ;go high above block pickup point 
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z46.5 ;raise block up to travel height
G1 X98.0 Y122.40000000000002 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z46.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z46.5 ;raise block up to travel height
G1 X161.5 Y185.9 ;go to block placement point
G1 Z16.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z46.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z71.9 ;raise block up to travel height
G1 X110.7 Y135.10000000000002 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z71.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z71.9 ;raise block up to travel height
G1 X148.8 Y173.20000000000002 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z71.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z71.9 ;raise block up to travel height
G1 X98.0 Y122.40000000000002 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z71.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z71.9 ;raise block up to travel height
G1 X148.8 Y173.20000000000002 ;go to block placement point
G1 Z41.9 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z71.9 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z97.3 ;raise block up to travel height
G1 X136.1 Y160.5 ;go to block placement point
G1 Z67.3 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z97.3 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z97.3 ;raise block up to travel height
G1 X110.7 Y135.10000000000002 ;go to block placement point
G1 Z67.3 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z97.3 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z97.3 ;raise block up to travel height
G1 X174.2 Y198.60000000000002 ;go to block placement point
G1 Z67.3 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z97.3 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z122.69999999999999 ;raise block up to travel height
G1 X148.8 Y173.20000000000002 ;go to block placement point
G1 Z92.69999999999999 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z122.69999999999999 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z122.69999999999999 ;raise block up to travel height
G1 X148.8 Y173.20000000000002 ;go to block placement point
G1 Z92.69999999999999 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z122.69999999999999 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z148.1 ;raise block up to travel height
G1 X148.8 Y173.20000000000002 ;go to block placement point
G1 Z118.1 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z148.1 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 Z46.5 ;go high above block pickup point
G1 Z16.5 ; descend to block pickup point height
G1 E4 ;lock in gripper
G4 P500 ;pause
G1 Z173.5 ;raise block up to travel height
G1 X148.8 Y173.20000000000002 ;go to block placement point
G1 Z143.5 ;descend to block placement height
G1 E0 ;release gripper
G4 P500 ;pause
G1 Z173.5 ;raise empty gripper up to travel height
G4 P5000; long pause before next block pickup
 
G1 X34.5 Y224 ; finish by going back to block pickup corner but stay at final height
