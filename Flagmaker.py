from os import listdir
from PIL import Image, ImageChops, ImagePalette, ImageFilter
from PIL import ImageFilter

def main():
	d: bool = False
	s: int = 0
	onoff = input("Press 1 to Quit:\nPress 2 for Dithered Flags: ")
	if onoff == "1":
		quit
	elif onoff == "2":
		d: bool = True
	onoff = input("\nPress 1 to Quit:\nPress 2 for HoI2:\nPress 3 for DH:\n"+
	 "Press 4 for Vic1:\nPress 5 for EU3 style:\nPress 6 for HoI3 style: ")
	if onoff == "1":
		quit
	elif onoff == "2":
		s = 0
	elif onoff == "3":
		s = 1
	elif onoff == "4":
		s = 2
	elif onoff == "5":
		s = 3
	elif onoff == "6":
		s = 4
	start(d,s)

def start(d,s):
	list_dir = listdir('input')
#	list_dir = [f.lower() for f in list_dir]
	sorted(list_dir)
	for i in range(len(list_dir)):
		print(i)
		print(list_dir[i])
		try:
			imaging(list_dir[i],d,s)
		except Exception as e:
			print(f"Failed! \n {e}")

def imaging(img_source: str, dith: bool, _shield: int):
	try: #Load image!
		imb = Image.open(f"input\\{img_source}")
		imb = imb.convert('RGB')
	except Exception:
		print(f"Image {img_source} not found!")
		pass
	imbS = imb.copy()
	imbS = imbS.resize((70,44),resample=Image.BICUBIC)
	S_img = Image.new('RGB',(70,176))
	S_img.paste(imbS,(0,0))
	S_img.paste(imbS,(0,44))
	S_img.paste(imbS,(0,88))
	S_img.paste(imbS,(0,132))
	S_img = S_img.transpose(Image.ROTATE_270)
	S_img = S_img.convert('RGB')
	if _shield == 0:
		_S = Image.open(f"Shield_Blank.png")
	elif _shield == 1:
		_S = Image.open(f"Shield_BlankDH.png")
	elif _shield == 2:
		_S = Image.open(f"Shield_Blankvc.png")
	elif _shield == 3:
		_S = Image.open(f"Shield_BlankEU.png")
	elif _shield == 4:
		_S = Image.open(f"Shield_Blankhoi3.png")
	_S = _S.convert('RGB')
	S_img = ImageChops.multiply(S_img,_S)
	if _shield == 0:
		_S = Image.open(f"Shield_SCREEN.png")
	elif _shield == 1:
		_S = Image.open(f"Shield_dhSCREEN.png")
	elif _shield == 2:
		_S = Image.open(f"Shield_vcSCREEN.png")
	elif _shield == 3:
		_S = Image.open(f"Shield_euSCREEN.png")
	elif _shield == 4:
		_S = Image.open(f"Shield_hoi3SCREEN.png")
	S_img = S_img.convert('RGBA')
	S_img = ImageChops.screen(S_img,_S)
	_S = _S.convert('RGB')
	S_img.save(f'output\\shield\\shield_{img_source[0:-1-3]}.bmp',bits=24, optimize=True)
	_S = Image.open(f'output\\shield\\shield_{img_source[0:-1-3]}.bmp')
	_S.convert('RGB')
	_S.save(f'output\\shield\\shield_{img_source[0:-1-3]}.bmp',bits=24, optimize=True)
	imbF = imb.copy()#.convert('RGBA', dither=Image.Dither)
	imbF = imbF.resize((25,18),resample=Image.BICUBIC)
	main.F_img = Image.new('RGBA',(700,18),(0,0,0,0))
	main.F_ = main.F_img.copy()
	for i in range(25):
		main.F_img.paste(imbF,(28*i,0))
#	F_img.save(f'0flag_output.bmp',bits=8, optimize=True)
	D1_U2 = ((0,6),(17,20),(23,25),(28,35),(46,49),(50,53),(56,63),(76,81),(84,92),(105,108),
	 (112,121),(134,135),(140,150),(168,179),(196,208),(224,237),(252,261),(263,266),(280,289),
	 (293,295),(308,317),(322,324),(336,345),(351,353),(364,374),(380,382),(392,403),(409,411),
	 (420,424),(428,431),(438,439),(448,451),(457,460),(467,468),(476,478),(486,489),(495,497),
	 (504,506),(515,517),(524,526),(532,534),(544,546),(553,554),(560,563),(573,575),(581,583),
	 (588,592),(602,604),(610,611),(616,621),(631,633),(638,640),(644,649),(660,662),(666,668),
	 (672,678),(689,692),(695,697))
#	new_ = "D1_U2 = ("
#	for i in range(len(D1_U2)):
#		new_ = new_ + f"({D1_U2[i][0]},{D1_U2[i][1]+1}),"
#		if i%9 == 0:
#			new_ = new_ + "\n"
#	with open('1TEMP.txt','w', encoding="utf-8-sig") as saving_file:
#		saving_file.write(f"{new_}")
	D1_U1 = ((6,11),(14,17),(35,39),(43,46),(63,67),(73,76),(92,96),(102,105),(108,109),(121,124),(131,134),(135,137),(150,153), 
	 (159,165),(179,181),(188,193),(207,210),(217,221),(237,239),(246,249),(266,268),(295,297),(324,336),(353,355),(382,384),
	 (411,413),(424,428),(439,442),(451,457),(468,471),(478,486),(497,500),(506,516),(526,528),(534,544),(554,556),
	 (563,573),(583,585),(592,602),(611,613),(621,631),(640,641),(649,655),(657,660),(668,669),(678,683),(686,689))
	D2_U1 =((11,14),(39,43),(67,73),(96,102),(124,126),(129,131),(153,155),(158,160),(181,183),(186,188),(210,212),
	 (215,217),(239,241),(244,246),(268,270),(272,277),(297,305),(326,332),(355,361),(384,389),(413,417),(442,445),
	 (471,473),(500,501),(528,529),(556,557),(655,657),(683,686))
	D0_U2 = ((20,23),(49,50),(261,263),(289,293),(317,322),(345,351),(374,380),(403,409),(431,438),
	 (460,467),(489,495),(517,524),(546,553),(575,581),(604,610),(633,638),(662,666),(692,695))
	D2_U0 = ((126,129),(155,158),(183,186),(212,215),(241,244),(270,272))
	crop_and_chop(D1_U2,3,(0,1))
	crop_and_chop(D1_U1,2,(0,1))
	crop_and_chop(D2_U1,3,(0,2))
	crop_and_chop(D0_U2,2,(0,0))
	crop_and_chop(D2_U0,2,(0,2))
	if dith == False:
		T_ = Image.open(f"FLAG_BLANK.png")
	elif dith == True:
		T_ = Image.open(f"DITHFLAG_BLANK.png")
	T_.convert('RGBA')
	main.F_ = ImageChops.multiply(main.F_,T_)
	T_ = Image.open(f"FLAG_GREEN.png")
	T_.convert('RGBA')
	if dith == False:
		main.F_.paste(T_,(0,0), mask=T_)
#	main.F_=main.F_.quantize(colors=256, method=2, kmeans=2, dither=255)
#	main.F_=main.F_.convert('P',palette=Image.ADAPTIVE,colors=256)
	if dith == True:
		main.F_=main.F_.convert('P',palette=Image.ADAPTIVE).quantize(colors=256, method=0, 
		 kmeans=1, dither=Image.Dither.FLOYDSTEINBERG)
	main.F_=main.F_.convert('RGB',palette=Image.ADAPTIVE)
	if dith == True:
		main.F_.paste(T_,(0,0), mask=T_)
	main.F_.save(f'output\\flag\\flag_{img_source[0:-1-3]}.bmp', optimize=True)

#	T_.save(f'0flag_output.png',bits=8, optimize=True)
#	for i in range(len(D1_U2)):
#		_T = F_img.crop((D1_U2[i][0],0,D1_U2[i][1]+1,18))
#		T_img.paste(_T,(D1_U2[i][0],0))
#	main.T_img = main.T_img.resize((700,15),resample=Image.BICUBIC)
#	main.F_.paste(T_img,(0,1))

def crop_and_chop(_coords: list,_resize: int,_rcoord: tuple):
	main.T_img = Image.new('RGBA',(700,18),(0,0,0,0))
	for i in range(len(_coords)):
#		print(_coords[i][0],0,_coords[i][1],18)
		_T = main.F_img.crop((_coords[i][0],0,_coords[i][1],18))
		main.T_img.paste(_T,(_coords[i][0],0))
	main.T_img = main.T_img.resize((700,18-_resize),resample=Image.LANCZOS)
	main.F_.paste(main.T_img,_rcoord,main.T_img)		

#	T_img = ImageChops.offset(T_img,0,1)
#0 28
#25 flag frames total
#Orange START:END

#Yellow
#Brown
#Blue
#Light Blue

if __name__ == '__main__':
	main()
