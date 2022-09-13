import turtle as tu

class trungthu:
    def __init__(self):
        self.r =[(12, 336) ,(17, 296) ,(27, 236) ,(34, 186) ,(41, 141) ,(54, 75) ,(117, 76) ,(132, 82) ,(143, 94) ,(149, 114) ,(149, 137) ,(145, 156) ,(141, 171) ,(136, 183) ,(123, 199) ,(102, 210) ,(106, 230) ,(110, 248) ,(115, 270) ,(120, 290) ,(125, 309) ,(129, 336) ,(94, 338) ,(65, 210) ,(46, 336) ,(12, 336)]
        self.r1 =[(83, 104) ,(80, 123) ,(76, 145) ,(73, 164) ,(72, 179) ,(68, 191) ,(79, 190) ,(92, 184) ,(100, 173) ,(107, 156) ,(110, 139) ,(112, 128) ,(110, 119) ,(101, 108) ,(89, 106) ,(82, 105) ,(82, 104)]
        self.o =[(285, 77) ,(264, 73) ,(239, 75) ,(221, 82) ,(206, 95) ,(193, 118) ,(185, 139) ,(176, 170) ,(168, 209) ,(165, 245) ,(163, 270) ,(164, 289) ,(169, 310) ,(176, 322) ,(184, 331) ,(192, 333) ,(200, 326) ,(200, 317) ,(192, 298) ,(186, 283) ,(186, 273) ,(186, 255) ,(189, 238) ,(191, 215) ,(191, 197) ,(195, 158) ,(218, 126) ,(239, 103) ,(263, 103) ,(287, 89) ,(286, 77)]
        self.c =[(411, 74) ,(420, 71) ,(435, 71) ,(446, 73) ,(454, 74) ,(464, 79) ,(461, 101) ,(440, 91) ,(420, 84) ,(407, 76) ,(411, 74)]
        self.k =[(483, 121) ,(486, 104) ,(488, 85) ,(489, 75) ,(507, 75) ,(524, 76) ,(523, 88) ,(521, 104) ,(518, 121) ,(515, 138) ,(513, 151) ,(512, 161) ,(510, 174) ,(510, 184) ,(510, 193) ,(522, 172) ,(534, 150) ,(548, 125) ,(558, 106) ,(568, 89) ,(575, 76) ,(590, 76) ,(611, 76) ,(600, 95) ,(588, 117) ,(572, 144) ,(557, 170) ,(545, 190) ,(538, 201) ,(544, 224) ,(551, 248) ,(560, 282) ,(567, 314) ,(573, 336) ,(531, 336) ,(520, 313) ,(520, 282) ,(516, 250) ,(509, 215) ,(509, 199) ,(512, 192)]
        self.y =[(618, 76) ,(621, 97) ,(626, 127) ,(634, 165) ,(640, 193) ,(645, 224) ,(639, 257) ,(635, 283) ,(632, 310) ,(628, 334) ,(646, 335) ,(661, 336) ,(668, 307) ,(671, 275) ,(679, 232) ,(681, 220) ,(692, 200) ,(707, 171) ,(720, 145) ,(730, 122) ,(742, 94) ,(752, 75) ,(735, 74) ,(716, 76) ,(704, 102) ,(694, 127) ,(686, 148) ,(677, 167) ,(669, 192) ,(663, 154) ,(660, 124) ,(656, 92) ,(655, 74) ,(637, 75) ,(618, 76)]
        self.boy1 =[(251, 299) ,(257, 291) ,(263, 279) ,(268, 264) ,(272, 248) ,(275, 236) ,(278, 228) ,(278, 220) ,(275, 215) ,(279, 210) ,(287, 204) ,(297, 200) ,(311, 204) ,(319, 208) ,(329, 210) ,(343, 212) ,(359, 212) ,(373, 211) ,(387, 214) ,(395, 219) ,(405, 226) ,(413, 234) ,(423, 240) ,(433, 245) ,(445, 248) ,(447, 252) ,(451, 259) ,(455, 266) ,(460, 271) ,(466, 278) ,(469, 286) ,(469, 300) ,(471, 312) ,(473, 322) ,(479, 336) ,(483, 346) ,(489, 351) ,(489, 360) ,(489, 366) ,(488, 375) ,(485, 384) ,(487, 393) ,(487, 405) ,(486, 414) ,(480, 422) ,(471, 429) ,(465, 432) ,(458, 436) ,(451, 437) ,(448, 434) ,(441, 428) ,(438, 423) ,(431, 417) ,(426, 416) ,(417, 415) ,(405, 413) ,(400, 412) ,(393, 407) ,(392, 403) ,(398, 395) ,(388, 396) ,(380, 402) ,(375, 408) ,(369, 410) ,(364, 410) ,(358, 410) ,(349, 410) ,(340, 414) ,(329, 420) ,(317, 425) ,(309, 431) ,(303, 438) ,(295, 451) ,(288, 453) ,(281, 453) ,(269, 451) ,(261, 448) ,(258, 441) ,(256, 437) ,(249, 428) ,(248, 417) ,(247, 405) ,(244, 390) ,(243, 379) ,(247, 361) ,(247, 351) ,(246, 332) ,(247, 325) ,(247, 310) ,(251, 301)]
        self.boy2 =[(264, 302) ,(270, 292) ,(272, 287) ,(273, 282) ,(280, 271) ,(286, 261) ,(288, 252) ,(279, 263) ,(284, 245) ,(288, 234) ,(295, 226) ,(305, 222) ,(316, 223) ,(331, 220) ,(342, 220) ,(358, 218) ,(375, 220) ,(391, 226) ,(403, 236) ,(413, 244) ,(422, 252) ,(413, 249) ,(399, 246) ,(409, 254) ,(417, 256) ,(404, 256) ,(394, 257) ,(389, 266) ,(381, 275) ,(381, 286) ,(381, 297) ,(389, 305) ,(380, 310) ,(377, 316) ,(379, 325) ,(373, 319) ,(368, 326) ,(368, 338) ,(368, 350) ,(369, 360) ,(369, 372) ,(369, 387) ,(369, 398) ,(369, 404) ,(361, 405) ,(358, 395) ,(358, 379) ,(358, 355) ,(358, 330) ,(358, 316) ,(355, 312) ,(344, 312) ,(342, 309) ,(340, 302) ,(340, 291) ,(334, 279) ,(326, 269) ,(316, 266) ,(308, 270) ,(293, 277) ,(282, 285) ,(275, 291) ,(269, 298) ,(264, 301)]
        self.boy3 =[(293, 447) ,(288, 430) ,(287, 407) ,(287, 382) ,(287, 365) ,(282, 360) ,(296, 353) ,(309, 345) ,(316, 342) ,(295, 340) ,(284, 335) ,(289, 336) ,(289, 336) ,(297, 338) ,(307, 337) ,(316, 335) ,(322, 333) ,(332, 331) ,(338, 329) ,(332, 325) ,(319, 319) ,(308, 318) ,(301, 318) ,(293, 321) ,(289, 323) ,(285, 327) ,(280, 331) ,(276, 338) ,(264, 347) ,(265, 335) ,(272, 316) ,(280, 309) ,(286, 306) ,(294, 306) ,(305, 307) ,(320, 308) ,(333, 308) ,(345, 318) ,(346, 328) ,(337, 340) ,(326, 352) ,(315, 363) ,(320, 362) ,(328, 359) ,(340, 351) ,(337, 364) ,(337, 374) ,(333, 378) ,(324, 384) ,(320, 391) ,(316, 397) ,(307, 410) ,(303, 420) ,(300, 431) ,(299, 438) ,(293, 446)]
        self.nose =[(313, 365) ,(325, 354) ,(342, 337) ,(349, 324) ,(342, 314) ,(331, 308) ,(348, 311) ,(357, 312) ,(357, 326) ,(356, 344) ,(357, 364) ,(357, 380) ,(359, 395) ,(361, 405) ,(368, 406) ,(369, 386) ,(367, 361) ,(367, 346) ,(368, 330) ,(371, 318) ,(379, 326) ,(387, 335) ,(398, 343) ,(406, 348) ,(420, 356) ,(410, 368) ,(403, 368) ,(395, 361) ,(390, 349) ,(384, 339) ,(375, 329) ,(373, 326) ,(373, 345) ,(374, 360) ,(373, 374) ,(374, 385) ,(375, 389) ,(377, 384) ,(382, 378) ,(387, 373) ,(392, 370) ,(397, 370) ,(399, 375) ,(401, 382) ,(402, 389) ,(399, 394) ,(392, 395) ,(384, 399) ,(379, 401) ,(374, 406) ,(369, 410) ,(361, 409) ,(354, 404) ,(348, 402) ,(341, 402) ,(336, 404) ,(330, 403) ,(329, 395) ,(330, 390) ,(338, 379) ,(336, 369) ,(338, 360) ,(338, 354) ,(326, 361) ,(315, 366)]
        self.nose1 =[(334, 404) ,(339, 404) ,(344, 403) ,(349, 404) ,(355, 407) ,(360, 410) ,(365, 412) ,(372, 409) ,(378, 405) ,(383, 401) ,(390, 398) ,(397, 395)]
        self.boy4 =[(372, 325) ,(372, 335) ,(372, 348) ,(372, 363) ,(373, 376) ,(373, 386) ,(381, 379) ,(387, 371) ,(393, 368) ,(397, 368) ,(404, 374) ,(411, 381) ,(416, 390) ,(421, 396) ,(426, 404) ,(429, 409) ,(432, 413) ,(439, 411) ,(446, 413) ,(452, 420) ,(454, 427) ,(456, 434) ,(464, 433) ,(472, 430) ,(478, 422) ,(480, 412) ,(479, 398) ,(477, 378) ,(470, 349) ,(470, 355) ,(465, 365) ,(461, 373) ,(458, 386) ,(449, 380) ,(437, 370) ,(431, 365) ,(423, 355) ,(418, 360) ,(411, 367) ,(404, 369) ,(394, 359) ,(390, 348) ,(387, 340) ,(381, 334) ,(374, 325)]
        self.dragon =[(401, 304) ,(408, 297) ,(413, 293) ,(398, 296) ,(390, 303) ,(381, 310) ,(375, 318) ,(379, 326) ,(389, 336) ,(396, 342) ,(405, 351) ,(413, 354) ,(421, 358) ,(427, 352) ,(421, 344) ,(430, 341) ,(442, 334) ,(429, 334) ,(412, 330) ,(409, 326) ,(420, 326) ,(433, 325) ,(449, 318) ,(439, 310) ,(423, 307) ,(410, 310) ,(402, 314) ,(394, 319) ,(390, 324) ,(399, 324) ,(406, 326) ,(411, 327)]
        self.eyebrowline =[(276, 329) ,(281, 323) ,(289, 318) ,(300, 316) ,(309, 315) ,(318, 315) ,(326, 317) ,(332, 320)]
        self.eyebrowline2 =[(393, 314) ,(400, 309) ,(407, 305) ,(418, 304) ,(430, 303) ,(436, 305) ,(446, 309) ,(455, 312)]
        self.ear1 =[(237, 356) ,(230, 359) ,(224, 362) ,(222, 367) ,(225, 377) ,(230, 384) ,(234, 390) ,(234, 400) ,(234, 409) ,(238, 417) ,(243, 423) ,(243, 416) ,(239, 407) ,(239, 400) ,(241, 391) ,(245, 382) ,(243, 372) ,(240, 364) ,(238, 356)]
        self.ear2 =[(226, 360) ,(225, 366) ,(226, 372) ,(231, 374) ,(233, 381) ,(235, 371) ,(235, 361) ,(238, 355) ,(231, 357) ,(226, 361)]
        self.ear3 =[(502, 353) ,(503, 362) ,(500, 371) ,(499, 379) ,(501, 385) ,(504, 388) ,(503, 377) ,(507, 369) ,(508, 363) ,(506, 359) ,(505, 355) ,(503, 353)]
        self.beard =[(326, 451) ,(330, 459) ,(337, 464) ,(346, 468) ,(355, 469) ,(368, 469) ,(381, 468) ,(395, 464) ,(406, 458) ,(412, 451) ,(411, 459) ,(413, 468) ,(419, 475) ,(417, 480) ,(405, 486) ,(390, 486) ,(378, 483) ,(371, 476) ,(362, 477) ,(351, 485) ,(345, 496) ,(334, 495) ,(322, 495) ,(317, 478) ,(316, 469) ,(323, 452)]
        self.face1 =[(223, 439) ,(210, 442) ,(195, 448) ,(177, 457) ,(160, 469) ,(143, 480) ,(123, 487) ,(104, 495) ,(87, 504) ,(71, 518) ,(61, 537) ,(51, 558) ,(40, 582) ,(33, 600) ,(23, 625) ,(20, 650) ,(19, 671) ,(12, 686) ,(11, 693) ,(23, 693) ,(40, 695) ,(55, 694) ,(77, 694) ,(93, 692) ,(114, 692) ,(146, 694) ,(177, 693) ,(246, 693) ,(361, 692) ,(501, 694) ,(565, 692) ,(635, 689) ,(710, 691) ,(750, 689) ,(744, 534) ,(727, 512) ,(710, 496) ,(695, 488) ,(667, 475) ,(642, 464) ,(616, 455) ,(596, 445) ,(576, 440) ,(552, 433) ,(522, 425) ,(514, 442) ,(506, 462) ,(502, 488) ,(494, 496) ,(490, 508) ,(485, 526) ,(478, 540) ,(467, 556) ,(454, 572) ,(436, 589) ,(421, 600) ,(401, 607) ,(379, 611) ,(360, 606) ,(337, 592) ,(321, 577) ,(319, 563) ,(302, 548) ,(289, 530) ,(274, 511) ,(261, 483) ,(251, 461) ,(232, 446) ,(228, 441) ,(222, 437)]
        self.face2 =[(19, 692) ,(16, 677) ,(14, 650) ,(14, 647) ,(23, 659) ,(31, 676) ,(34, 660) ,(32, 641) ,(32, 634) ,(41, 650) ,(46, 665) ,(54, 681) ,(62, 689) ,(73, 692) ,(80, 690) ,(72, 676) ,(56, 656) ,(45, 624) ,(45, 615) ,(59, 641) ,(73, 655) ,(79, 649) ,(70, 629) ,(70, 609) ,(70, 594) ,(79, 613) ,(86, 645) ,(96, 666) ,(102, 684) ,(106, 688) ,(114, 688) ,(121, 688) ,(118, 663) ,(100, 622) ,(82, 571) ,(73, 542) ,(85, 551) ,(99, 553) ,(112, 565) ,(121, 576) ,(132, 591) ,(134, 573) ,(112, 512) ,(147, 574) ,(157, 606) ,(168, 640) ,(172, 670) ,(177, 684) ,(179, 692) ,(189, 692) ,(195, 690) ,(187, 644) ,(164, 592) ,(147, 534) ,(134, 501) ,(149, 511) ,(166, 515) ,(180, 519) ,(191, 525) ,(194, 550) ,(190, 575) ,(192, 597) ,(194, 616) ,(201, 597) ,(202, 583) ,(196, 553) ,(196, 530) ,(194, 509) ,(183, 486) ,(179, 466) ,(195, 462) ,(205, 455) ,(211, 452) ,(222, 465) ,(228, 478) ,(228, 495) ,(228, 503) ,(241, 504) ,(250, 500) ,(258, 524) ,(266, 544) ,(274, 557) ,(288, 567) ,(303, 585) ,(318, 607) ,(330, 622) ,(343, 639) ,(358, 656) ,(383, 672) ,(405, 680) ,(413, 680) ,(420, 678) ,(429, 674) ,(423, 665) ,(387, 659) ,(403, 650) ,(405, 634) ,(400, 627) ,(402, 610) ,(414, 610) ,(431, 597) ,(447, 586) ,(456, 574) ,(468, 559) ,(485, 538) ,(496, 519) ,(498, 499) ,(502, 493) ,(504, 480) ,(517, 466) ,(525, 460) ,(532, 451) ,(532, 465) ,(531, 487) ,(531, 514) ,(535, 514) ,(547, 495) ,(553, 473) ,(553, 456) ,(554, 446) ,(562, 469) ,(563, 487) ,(556, 512) ,(560, 546) ,(570, 532) ,(577, 505) ,(587, 491) ,(600, 484) ,(611, 482) ,(623, 483) ,(636, 481) ,(646, 482) ,(651, 483) ,(659, 486) ,(647, 492) ,(619, 495) ,(614, 507) ,(597, 520) ,(596, 528) ,(592, 540) ,(588, 562) ,(589, 571) ,(594, 584) ,(595, 606) ,(598, 617) ,(600, 642) ,(608, 637) ,(617, 614) ,(623, 595) ,(634, 565) ,(651, 537) ,(655, 528) ,(670, 515) ,(683, 514) ,(692, 511) ,(710, 512) ,(693, 503) ,(684, 495) ,(697, 489) ,(708, 484) ,(720, 493) ,(723, 495) ,(735, 504) ,(755, 517) ,(752, 538) ,(752, 559) ,(749, 573) ,(735, 587) ,(722, 597) ,(700, 611) ,(712, 590) ,(714, 570) ,(714, 566) ,(695, 569) ,(688, 600) ,(686, 617) ,(682, 631) ,(681, 652) ,(698, 645) ,(704, 627) ,(721, 608) ,(740, 591) ,(749, 591) ,(742, 613) ,(725, 635) ,(717, 647) ,(710, 667) ,(738, 659) ,(742, 658) ,(720, 672) ,(719, 685) ,(751, 675) ,(746, 686) ,(695, 687) ,(668, 690) ,(614, 686) ,(566, 686) ,(511, 690) ,(481, 691) ,(430, 689) ,(358, 680) ,(325, 688) ,(273, 686) ,(233, 684) ,(191, 689) ,(164, 683) ,(162, 689) ,(140, 690) ,(113, 684) ,(80, 686) ,(47, 692) ,(32, 691) ,(11, 685)]
        self.face3 =[(20, 686) ,(23, 679) ,(23, 657) ,(39, 677) ,(42, 679) ,(43, 659) ,(45, 637) ,(54, 645) ,(69, 668) ,(78, 677) ,(87, 686) ,(88, 674) ,(83, 641) ,(81, 625) ,(81, 608) ,(83, 586) ,(85, 580) ,(90, 607) ,(99, 630) ,(124, 664) ,(132, 671) ,(132, 653) ,(125, 618) ,(114, 600) ,(103, 580) ,(138, 622) ,(146, 637) ,(152, 660) ,(155, 663) ,(157, 636) ,(157, 629) ,(149, 586) ,(148, 579) ,(145, 573) ,(187, 623) ,(206, 650) ,(238, 684) ,(234, 678) ,(228, 643) ,(228, 610) ,(228, 583) ,(218, 529) ,(209, 504) ,(229, 522) ,(249, 562) ,(258, 613) ,(260, 631) ,(265, 654) ,(273, 676) ,(274, 679) ,(278, 678) ,(285, 641) ,(282, 620) ,(279, 593) ,(256, 550) ,(281, 613) ,(293, 640) ,(301, 656) ,(321, 674) ,(323, 680) ,(344, 686) ,(358, 688) ,(386, 684) ,(428, 688) ,(430, 670) ,(419, 632) ,(420, 621) ,(456, 658) ,(457, 663) ,(462, 670) ,(470, 639) ,(469, 619) ,(456, 594) ,(477, 614) ,(492, 647) ,(497, 654) ,(501, 663) ,(514, 645) ,(517, 609) ,(518, 580) ,(519, 542) ,(529, 558) ,(539, 650) ,(539, 665) ,(552, 596) ,(565, 565) ,(583, 536) ,(608, 522) ,(631, 514) ,(613, 542) ,(591, 600) ,(587, 640) ,(591, 647) ,(597, 665) ,(601, 666) ,(620, 643) ,(627, 614) ,(629, 590) ,(625, 528) ,(615, 490) ,(671, 551) ,(679, 605) ,(671, 636) ,(670, 656) ,(675, 656) ,(693, 599) ,(695, 572) ,(691, 538) ,(681, 519) ,(698, 550) ,(715, 608) ,(727, 659) ,(723, 679) ,(721, 686) ,(692, 686) ,(675, 683) ,(634, 685) ,(589, 685) ,(547, 681) ,(476, 681) ,(414, 680) ,(363, 680) ,(315, 673) ,(244, 673) ,(208, 677) ,(135, 677) ,(95, 677) ,(49, 677) ,(21, 676)]
        self.face4 =[(327, 452) ,(321, 458) ,(315, 466) ,(316, 473) ,(319, 479) ,(320, 487) ,(322, 478) ,(323, 490) ,(327, 482) ,(328, 490) ,(324, 497) ,(336, 488) ,(335, 494) ,(342, 484) ,(343, 492) ,(351, 484) ,(354, 479) ,(350, 480) ,(358, 477) ,(365, 476) ,(371, 473) ,(376, 479) ,(380, 484) ,(380, 479) ,(385, 484) ,(395, 487) ,(390, 478) ,(398, 482) ,(398, 477) ,(405, 482) ,(410, 488) ,(408, 471) ,(414, 480) ,(413, 474) ,(419, 477) ,(411, 466) ,(412, 459) ,(405, 463) ,(403, 468) ,(397, 469) ,(391, 473) ,(383, 472) ,(369, 472) ,(358, 473) ,(349, 476) ,(343, 481) ,(336, 481) ,(331, 467) ,(341, 466) ,(334, 460) ,(326, 451)]
        self.neck =[(328, 581) ,(335, 590) ,(343, 596) ,(352, 603) ,(361, 608) ,(374, 612) ,(390, 611) ,(408, 605) ,(424, 597) ,(440, 586) ,(461, 562) ,(479, 539) ,(488, 520) ,(488, 506) ,(485, 494) ,(474, 514) ,(459, 532) ,(432, 553) ,(399, 569) ,(366, 575) ,(332, 573) ,(330, 578) ,(328, 581)]
        self.hair1 = [(182, 356) ,(193, 360) ,(205, 361) ,(220, 362) ,(229, 359) ,(235, 356) ,(235, 366) ,(236, 376) ,(237, 382) ,(237, 389) ,(241, 383) ,(241, 378) ,(244, 375) ,(242, 371) ,(240, 366) ,(240, 363) ,(244, 369) ,(248, 369) ,(246, 365) ,(245, 358) ,(246, 335) ,(247, 328) ,(253, 335) ,(249, 322) ,(248, 312) ,(249, 302) ,(255, 295) ,(261, 284) ,(267, 269) ,(270, 260) ,(273, 245) ,(277, 235) ,(279, 224) ,(277, 216) ,(285, 205) ,(296, 203) ,(307, 203) ,(303, 206) ,(312, 206) ,(325, 210) ,(338, 213) ,(349, 213) ,(363, 211) ,(385, 215) ,(403, 226) ,(419, 237) ,(433, 246) ,(446, 249) ,(454, 262) ,(463, 271) ,(469, 288) ,(471, 312) ,(478, 335) ,(485, 347) ,(488, 351) ,(488, 359) ,(490, 373) ,(486, 384) ,(487, 397) ,(487, 402) ,(491, 409) ,(484, 402) ,(487, 412) ,(478, 422) ,(472, 430) ,(471, 422) ,(466, 429) ,(461, 432) ,(459, 437) ,(453, 437) ,(446, 437) ,(438, 426) ,(431, 417) ,(414, 414) ,(400, 413) ,(389, 401) ,(398, 395) ,(390, 397) ,(380, 401) ,(373, 409) ,(367, 411) ,(358, 408) ,(347, 409) ,(326, 417) ,(336, 418) ,(326, 422) ,(321, 420) ,(314, 428) ,(311, 430) ,(311, 425) ,(305, 438) ,(303, 431) ,(301, 442) ,(296, 448) ,(291, 457) ,(293, 447) ,(287, 455) ,(289, 448) ,(283, 453) ,(279, 446) ,(280, 452) ,(274, 454) ,(270, 450) ,(266, 450) ,(270, 445) ,(261, 450) ,(265, 443) ,(257, 447) ,(261, 436) ,(261, 431) ,(255, 434) ,(254, 428) ,(250, 428) ,(255, 419) ,(250, 425) ,(256, 415) ,(250, 418) ,(250, 405) ,(249, 415) ,(247, 402) ,(247, 395) ,(246, 387) ,(241, 395) ,(238, 401) ,(243, 409) ,(243, 421) ,(234, 396) ,(228, 385) ,(222, 366) ,(220, 364) ,(213, 363) ,(203, 366) ,(193, 372) ,(198, 381) ,(194, 398) ,(205, 377) ,(208, 379) ,(205, 387) ,(204, 406) ,(215, 431) ,(207, 417) ,(212, 404) ,(219, 395) ,(223, 386) ,(221, 405) ,(217, 415) ,(218, 424) ,(224, 418) ,(226, 410) ,(226, 425) ,(219, 441) ,(222, 441) ,(223, 450) ,(227, 446) ,(231, 454) ,(236, 466) ,(243, 474) ,(249, 480) ,(252, 485) ,(250, 499) ,(252, 514) ,(255, 505) ,(263, 519) ,(269, 526) ,(273, 536) ,(283, 547) ,(287, 555) ,(288, 551) ,(296, 556) ,(302, 564) ,(309, 570) ,(318, 572) ,(326, 585) ,(328, 580) ,(345, 588) ,(337, 583) ,(353, 587) ,(373, 593) ,(360, 586) ,(370, 589) ,(387, 591) ,(384, 587) ,(405, 586) ,(393, 585) ,(409, 581) ,(397, 581) ,(409, 579) ,(419, 579) ,(408, 575) ,(432, 573) ,(422, 572) ,(439, 568) ,(434, 567) ,(442, 564) ,(435, 562) ,(449, 556) ,(457, 544) ,(457, 553) ,(463, 540) ,(468, 532) ,(479, 519) ,(478, 509) ,(479, 523) ,(484, 508) ,(485, 498) ,(491, 508) ,(495, 496) ,(503, 485) ,(501, 480) ,(511, 483) ,(502, 474) ,(512, 476) ,(503, 470) ,(516, 474) ,(506, 469) ,(518, 470) ,(508, 465) ,(524, 468) ,(514, 463) ,(530, 457) ,(516, 459) ,(526, 454) ,(521, 450) ,(547, 444) ,(524, 441) ,(541, 441) ,(528, 438) ,(540, 435) ,(551, 433) ,(539, 431) ,(552, 420) ,(539, 425) ,(531, 426) ,(542, 419) ,(524, 421) ,(532, 417) ,(526, 416) ,(539, 412) ,(518, 414) ,(508, 403) ,(510, 388) ,(520, 409) ,(516, 386) ,(521, 375) ,(522, 366) ,(531, 379) ,(526, 361) ,(526, 353) ,(539, 336) ,(546, 313) ,(548, 290) ,(553, 277) ,(577, 270) ,(554, 268) ,(562, 265) ,(546, 264) ,(552, 261) ,(557, 255) ,(547, 259) ,(557, 247) ,(540, 248) ,(551, 236) ,(539, 240) ,(542, 233) ,(536, 226) ,(534, 214) ,(528, 202) ,(522, 199) ,(530, 198) ,(520, 190) ,(546, 194) ,(522, 187) ,(531, 183) ,(517, 184) ,(528, 176) ,(517, 181) ,(524, 177) ,(511, 178) ,(514, 174) ,(515, 151) ,(513, 160) ,(504, 153) ,(494, 136) ,(480, 121) ,(472, 113) ,(475, 106) ,(472, 107) ,(459, 93) ,(463, 102) ,(446, 92) ,(428, 81) ,(403, 74) ,(376, 71) ,(346, 70) ,(317, 81) ,(291, 77) ,(270, 88) ,(240, 92) ,(224, 101) ,(233, 98) ,(218, 114) ,(207, 131) ,(199, 146) ,(188, 161) ,(179, 185) ,(176, 219) ,(176, 243) ,(179, 263) ,(172, 273) ,(174, 293) ,(179, 311) ,(190, 320) ,(190, 325) ,(185, 328) ,(191, 337) ,(189, 347) ,(183, 353) ,(182, 354)]
        self.lips = [(327, 451) ,(337, 462) ,(351, 469) ,(370, 469) ,(387, 465) ,(404, 459) ,(411, 451) ,(401, 442) ,(391, 437) ,(383, 434) ,(377, 433) ,(370, 436) ,(365, 435) ,(360, 434) ,(354, 434) ,(347, 436) ,(342, 440) ,(336, 445) ,(327, 452) ,(339, 449) ,(350, 448) ,(361, 449) ,(371, 450) ,(382, 449) ,(392, 445) ,(402, 445) ,(390, 450) ,(379, 454) ,(366, 455) ,(356, 455) ,(345, 453) ,(336, 453) ,(332, 453)]
        self.lips1 =[(338, 462) ,(336, 456) ,(335, 452) ,(341, 453) ,(350, 453) ,(359, 454) ,(370, 454) ,(379, 453) ,(387, 451) ,(397, 449) ,(403, 446) ,(393, 446) ,(381, 449) ,(372, 451) ,(366, 449) ,(358, 449) ,(350, 449) ,(342, 449) ,(332, 450) ,(329, 451) ,(333, 457) ,(337, 461)]
        self.lips2 =[(337, 463) ,(337, 459) ,(337, 453) ,(345, 454) ,(356, 455) ,(366, 455) ,(377, 454) ,(386, 453) ,(396, 449) ,(401, 449) ,(407, 451) ,(401, 455) ,(395, 460) ,(388, 457) ,(383, 457) ,(377, 458) ,(373, 462) ,(368, 466) ,(364, 466) ,(361, 464) ,(355, 459) ,(351, 459) ,(344, 459) ,(342, 459) ,(342, 464) ,(340, 464) ,(337, 463)]
        self.eye1 =[(279, 335) ,(289, 326) ,(298, 321) ,(306, 319) ,(315, 320) ,(328, 324) ,(336, 328) ,(325, 330) ,(313, 334) ,(299, 337) ,(290, 335) ,(284, 331)]
        self.eyelid =[(294, 323) ,(295, 329) ,(304, 329) ,(305, 332) ,(301, 332) ,(297, 332) ,(304, 336) ,(310, 335) ,(316, 329) ,(316, 320) ,(306, 319) ,(299, 320) ,(295, 323)]
        self.eyelid2 =[(298, 324) ,(300, 325) ,(300, 328) ,(297, 328) ,(296, 327) ,(296, 325)]
        self.eye2 =[(390, 323) ,(397, 319) ,(407, 313) ,(417, 309) ,(426, 309) ,(436, 310) ,(442, 314) ,(447, 317) ,(439, 322) ,(430, 324) ,(418, 325) ,(407, 325) ,(400, 323) ,(391, 324)]
        self.eyelid3 =[(408, 313) ,(409, 318) ,(420, 319) ,(420, 321) ,(411, 322) ,(415, 325) ,(419, 325) ,(424, 325) ,(430, 320) ,(432, 314) ,(429, 310) ,(422, 310) ,(418, 310) ,(413, 311) ,(409, 313)]
        self.eyelid4 =[(410, 314) ,(412, 314) ,(411, 316) ,(409, 316) ,(409, 314)]
        self.eyebrow1 =[(261, 312) ,(266, 306) ,(277, 301) ,(288, 299) ,(305, 301) ,(315, 302) ,(324, 304) ,(320, 299) ,(328, 306) ,(323, 295) ,(331, 306) ,(335, 306) ,(329, 293) ,(321, 290) ,(309, 288) ,(297, 288) ,(283, 292) ,(287, 289) ,(292, 287) ,(297, 286) ,(293, 286) ,(289, 287) ,(285, 288) ,(277, 292) ,(273, 296) ,(268, 301) ,(264, 305) ,(261, 309)]
        self.eyebrow2 =[(393, 299) ,(397, 289) ,(406, 279) ,(421, 275) ,(440, 276) ,(433, 273) ,(442, 275) ,(452, 280) ,(460, 288) ,(463, 293) ,(453, 285) ,(446, 285) ,(432, 288) ,(422, 290) ,(407, 293) ,(395, 298)]
        self.mouth = [(374, 382),(368, 382),(359, 382),(347, 379),(339, 381),(334, 384),(323, 380),(315, 380),(293, 385),(321, 387),(339, 387),(345, 386),(357, 385),(374, 383),(-1, -1),(389, 389),(393, 387),(395, 381),(395, 373),(377, 362),(366, 357),(358, 360),(351, 357),(345, 354),(344, 357),(337, 355),(333, 357),(327, 355),(323, 357),(303, 362),(293, 365),(286, 367),(282, 374),(277, 376),(279, 394),(286, 390),(293, 380),(297, 378),(302, 378),(304, 375),(307, 378),(310, 374),(313, 377),(315, 373),(319, 375),(322, 374),(325, 376),(329, 375),(336, 375),(342, 374),(350, 374),(353, 376),(357, 374),(369, 374),(372, 377),(374, 374),(377, 378),(383, 379),(389, 389),]
        self.nose = [(342, 305),(342, 313),(344, 321),(344, 328),(343, 335),(338, 342),(331, 344),(322, 343),(313, 340),(310, 339),(307, 339),(303, 333),(301, 338),(305, 343),(313, 344),(323, 349),(332, 353),(343, 345),(346, 342),(354, 342),(359, 338),(360, 329),(355, 322),(348, 320),(348, 323),(354, 325),(356, 331),(353, 336),(348, 335),(350, 330),(348, 323),(343, 305),]
        self.dress = [(56, 513),(222, 433),(247, 393),(249, 408),(254, 425),(265, 456),(265, 456),(273, 478),(280, 495),(283, 509),(294, 539),(302, 527),(314, 515),(328, 503),(347, 491),(350, 493),(340, 499),(349, 507),(359, 517),(380, 498),(397, 505),(412, 516),(425, 526),(432, 533),(435, 539),(399, 523),(399, 530),(395, 538),(353, 539),(347, 530),(320, 519),(300, 539),(293, 539),(-1, -1),(363, 507),(391, 478),(401, 458),(422, 408),(423, 398),(420, 407),(400, 440),(386, 460),(377, 471),(371, 475),(366, 480),(357, 482),(348, 478),(339, 470),(330, 462),(316, 453),(301, 444),(276, 420),(248, 391),(253, 399),(267, 419),(278, 430),(288, 441),(295, 445),(303, 453),(326, 475),(338, 484),(347, 492),(353, 498),(363, 508),(371, 500),(-1, -1),(427, 401),(437, 486),(441, 526),(443, 539),(624, 539),(625, 477),(528, 449),(477, 428),(447, 412),(428, 401),]
        self.face = [(328, 461),(316, 457),(305, 453),(297, 446),(286, 436),(284, 434),(280, 431),(277, 431),(279, 428),(275, 428),(272, 423),(262, 411),(250, 395),(244, 387),(241, 382),(238, 377),(235, 372),(236, 367),(234, 363),(234, 358),(231, 354),(231, 349),(230, 346),(231, 343),(228, 339),(229, 336),(226, 330),(227, 324),(223, 320),(224, 317),(221, 311),(216, 310),(212, 306),(213, 302),(216, 308),(220, 306),(220, 297),(217, 294),(219, 284),(216, 279),(216, 272),(211, 266),(208, 272),(206, 266),(207, 256),(205, 249),(204, 243),(204, 237),(208, 233),(208, 229),(206, 229),(206, 222),(202, 215),(202, 210),(197, 204),(198, 197),(193, 193),(192, 173),(190, 170),(191, 166),(190, 162),(191, 159),(188, 154),(186, 148),(188, 142),(188, 135),(188, 127),(191, 122),(186, 121),(177, 112),(185, 115),(179, 105),(188, 114),(182, 98),(191, 109),(194, 104),(200, 101),(194, 99),(203, 94),(206, 85),(211, 82),(218, 80),(213, 78),(208, 79),(212, 76),(218, 76),(216, 69),(218, 64),(219, 70),(221, 75),(223, 68),(230, 64),(231, 58),(234, 56),(235, 52),(236, 47),(240, 42),(242, 35),(252, 32),(270, 28),(283, 28),(290, 28),(297, 29),(304, 33),(318, 29),(332, 28),(346, 27),(356, 27),(366, 29),(379, 36),(363, 24),(375, 26),(389, 36),(397, 40),(405, 45),(411, 54),(422, 61),(429, 70),(433, 83),(435, 91),(436, 79),(436, 99),(436, 106),(441, 99),(435, 113),(450, 108),(469, 111),(477, 108),(473, 114),(467, 126),(477, 120),(479, 124),(471, 132),(473, 136),(472, 145),(483, 148),(479, 151),(480, 161),(483, 168),(480, 173),(480, 178),(476, 184),(474, 190),(472, 196),(465, 197),(462, 204),(462, 211),(461, 217),(459, 224),(463, 231),(456, 229),(452, 237),(449, 245),(448, 254),(448, 262),(450, 257),(452, 251),(454, 244),(458, 239),(462, 243),(462, 251),(458, 246),(456, 251),(454, 255),(458, 257),(452, 266),(454, 273),(455, 282),(452, 288),(453, 296),(458, 286),(457, 295),(453, 303),(449, 304),(448, 297),(450, 290),(453, 280),(448, 273),(448, 280),(446, 288),(445, 300),(444, 308),(448, 315),(454, 311),(454, 317),(449, 319),(443, 316),(442, 327),(439, 339),(437, 350),(433, 362),(430, 370),(430, 378),(426, 385),(420, 393),(416, 399),(411, 404),(408, 409),(403, 414),(399, 419),(394, 427),(386, 435),(381, 441),(376, 444),(371, 448),(367, 451),(359, 456),(352, 458),(348, 461),(341, 461),(336, 463),(330, 459),(328, 462),(316, 457),]
        self.iface = [(311, 400),(324, 402),(338, 402),(347, 402),(356, 399),(363, 397),(359, 402),(356, 408),(353, 414),(348, 419),(349, 426),(359, 426),(362, 430),(367, 433),(374, 434),(376, 436),(379, 432),(383, 433),(385, 427),(393, 419),(394, 416),(398, 413),(400, 408),(401, 394),(408, 402),(415, 394),(421, 385),(424, 380),(424, 373),(427, 367),(432, 353),(434, 345),(436, 339),(434, 330),(438, 322),(438, 312),(437, 310),(440, 309),(441, 293),(443, 288),(441, 284),(444, 275),(440, 265),(442, 233),(439, 227),(439, 221),(434, 211),(425, 203),(432, 203),(421, 192),(430, 196),(421, 187),(430, 187),(419, 178),(432, 180),(420, 172),(428, 174),(422, 165),(415, 159),(413, 147),(408, 140),(403, 140),(402, 138),(395, 139),(394, 136),(388, 138),(386, 136),(379, 138),(377, 133),(372, 134),(369, 131),(364, 134),(360, 133),(355, 135),(353, 131),(348, 132),(347, 127),(346, 131),(343, 127),(336, 131),(331, 128),(327, 130),(323, 126),(319, 129),(313, 125),(309, 131),(306, 126),(303, 131),(297, 126),(296, 131),(289, 127),(287, 130),(282, 126),(280, 132),(274, 128),(274, 135),(268, 131),(264, 135),(256, 134),(256, 139),(251, 138),(252, 142),(246, 142),(247, 146),(244, 149),(245, 154),(239, 154),(243, 160),(236, 163),(242, 164),(233, 169),(238, 170),(231, 177),(237, 176),(227, 184),(237, 180),(229, 190),(237, 189),(229, 198),(237, 195),(232, 202),(239, 205),(229, 212),(238, 210),(232, 215),(238, 215),(233, 220),(227, 227),(224, 237),(224, 246),(226, 253),(226, 259),(227, 267),(227, 277),(224, 291),(223, 304),(225, 311),(228, 319),(231, 330),(234, 340),(235, 349),(237, 361),(241, 372),(248, 385),(252, 391),(258, 397),(264, 402),(268, 396),(272, 398),(272, 406),(279, 414),(278, 419),(284, 426),(292, 431),(292, 435),(296, 438),(299, 438),(301, 442),(308, 439),(313, 435),(317, 435),(319, 430),(321, 428),(325, 426),(327, 426),(332, 424),(331, 416),(326, 416),(318, 408),(318, 404),(311, 400),(324, 402),]
        self.ebrow = [(339, 243),(339, 248),(343, 254),(350, 256),(358, 251),(367, 248),(382, 247),(397, 249),(407, 252),(418, 258),(419, 253),(414, 245),(399, 235),(391, 235),(381, 237),(372, 238),(361, 243),(353, 245),(343, 255),(-1, -1),(321, 246),(320, 258),(314, 257),(305, 254),(263, 253),(245, 259),(243, 257),(246, 250),(253, 245),(260, 242),(269, 241),(276, 241),(282, 243),(291, 245),(305, 245),(311, 249),(319, 252),(322, 246),]
        self.lines = [(345, 313),(344, 308),(343, 297),(343, 282),(-1, -1),(367, 340),(384, 357),(-1, -1),(295, 337),(280, 359),(-1, -1),(385, 278),(394, 278),(400, 273),(408, 264),(400, 261),(389, 257),(377, 258),(371, 260),(358, 269),(362, 272),(-1, -1),(395, 257),(371, 254),(353, 263),(-1, -1),(303, 274),(309, 273),(297, 263),(290, 262),(272, 262),(261, 270),(256, 271),(262, 271),(269, 277),(283, 281),(-1, -1),(255, 267),(271, 260),(282, 259),(291, 259),(300, 260),(311, 264),]
        self.eyes = [(375, 260),(375, 266),(378, 271),(384, 273),(389, 270),(391, 267),(392, 264),(391, 260),(388, 258),(384, 257),(379, 257),(375, 261),(-1,-1),(291, 263),(292, 269),(289, 273),(286, 276),(281, 276),(276, 273),(274, 269),(274, 265),(276, 263),(281, 262),(287, 262),(291, 263),]
        self.eball = [(281, 266),(279, 267),(277, 266),(277, 264),(279, 263),(281, 264),(281, 266),(-1, -1),(379, 259),(382, 260),(382, 263),(380, 264),(378, 263),(377, 261),(379, 259),]
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = 400
        self.y_offset = 400


    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        self.pen.pendown()  


    def paint(self,coord,co=(0,0,0)):
        self.pen.color(co)
        t_x,t_y = coord[0]
        self.go(t_x,t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x,y = i
            if t:
                self.go(x,y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset) 
        self.pen.end_fill()


    def draw_fn(self,coord,mode = 1,co = (0,0,0),thickness = 1):
        co = (co[0]/255,co[1]/255,co[2]/255)

        self.pen.color(co)

        if mode:
            self.pen.width(thickness)
            t_x,t_y = coord[0]
            self.go(t_x,t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x,y = i
                if t:
                    self.go(x,y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        else:
            self.paint(coord=coord,co = co)

    def draw(self,retain=True):
        self.draw_fn(self.r,co =(237, 7, 7),mode=0)
        self.draw_fn(self.r1,co =(247, 247, 247),mode=0)
        self.draw_fn(self.o,co =(237, 7, 7),mode=0)
        self.draw_fn(self.c,co =(237, 7, 7),mode=0)
        self.draw_fn(self.k,co =(237, 7, 7),mode=0)
        self.draw_fn(self.y,co =(237, 7, 7),mode=0)
        self.draw_fn(self.boy1,co =(239, 203, 184),mode=0)
        self.draw_fn(self.boy2,co =(228, 174, 146),mode=0)
        self.draw_fn(self.boy3,co =(228, 174, 146),mode=0)
        self.draw_fn(self.nose,co =(233, 187, 164),mode=0)
        self.draw_fn(self.nose1,co =(58, 35, 34),mode=1,thickness=2)
        self.draw_fn(self.boy4,co=(228, 174, 146),mode=0)
        self.draw_fn(self.rong,co=(228, 174, 146),mode=0)
        self.draw_fn(self.eyebrowline,co =(15, 14, 14),mode=1,thickness=2)
        self.draw_fn(self.eyebrowline2,co =(15, 14, 14),mode=1,thickness=2)
        self.draw_fn(self.shirt,co=(61, 184, 179),mode=0)
        self.draw_fn(self.shirt1,co=(48, 167, 161),mode=0)
        self.draw_fn(self.shirt2,co=(41, 121, 118),mode=0)
        self.draw_fn(self.neck,co=(225, 164, 143),mode=0)
        self.draw_fn(self.hair1,co = (57, 35, 37),mode = 0)
        self.draw_fn(self.beard,co=(227, 174, 143),mode=0)
        self.draw_fn(self.beard1,co=(178, 116, 100),mode=0)
        self.draw_fn(self.ear1,co = (230, 171, 139),mode = 0)
        self.draw_fn(self.ear2,co = (183, 121, 96),mode = 0)
        self.draw_fn(self.ear3,co = (230, 171, 139),mode = 0)
        self.draw_fn(self.lips,co = (184, 88, 89),mode = 0)
        self.draw_fn(self.lips1,co = (61, 31, 33),mode = 0)
        self.draw_fn(self.lips2,co = (149, 63, 66),mode = 0)
        self.draw_fn(self.eye1,co = (58, 35, 34),mode = 1,thickness=2)
        self.draw_fn(self.eyelid,co = (58, 35, 34),mode = 0)
        self.draw_fn(self.eyelid2,co = (255, 244, 243),mode = 0)
        self.draw_fn(self.eye2,co = (58, 35, 34),mode = 1,thickness=2)
        self.draw_fn(self.eyelid3,co = (58, 35, 34),mode = 0)
        self.draw_fn(self.eyelid4,co = (255, 244, 243),mode = 0)
        self.draw_fn(self.eyebrow1,co = (58, 35, 33),mode = 0)
        self.draw_fn(self.eyebrow2,co = (58, 35, 33),mode = 0)

        if retain:
            tu.done()

pen=trungthu()
pen.draw()