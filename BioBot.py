from random import randint
from math import sin, cos, radians


class Bot1():
	def __init__(self):
		self.min_val, self.max_val = 1, 360
		self.size_getter_eng = 10
		self.create_pos_bot(0, 500, 500)
		self.create_gen_bot()
		self.create_gen_bot()
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)

	def create_gen_bot(self):
		self.l1, self.l2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.w1, self.w2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.s1, self.s2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.a1, self.a2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.hp, self.eng = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2,
						 self.w1, self.w2,
						 self.s1, self.s2,
						 self.a1, self.a2,
						 self.hp, self.eng]

	def create_pos_bot(self, min_x, max_x, y):
		self.pos = (randint(min_x, max_x), y)

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.size_getter_eng / 2, self.pos[
			1] - self.l1 - self.l2 - self.size_getter_eng / 2, self.size_getter_eng, self.size_getter_eng
		return x1, y1, w, h

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg, master, color_l1, color_l2, color_eng):
		ang1 = self.edit_ang_l1()
		ang2 = self.edit_ang_l2()
		l1 = self.move_l1(ang1)
		l2 = self.move_l2(ang2)
		ge = self.move_getter_eng()
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def edit_ang_l1(self):
		# if 180 < self.a1 < 360:
		self.a1 += 1
		return self.a1

	def edit_ang_l2(self):
		# if 180 < self.a2 < 360:
		self.a2 -= 1
		return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def move_l1(self, ang):
		x1, y1 = self.pos[0], self.pos[1]
		x2 = x1 + cos(radians(ang)) * self.l1
		y2 = y1 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_getter_eng(self):
		return (self.l2_pos[2], self.l2_pos[3], self.size_getter_eng, self.size_getter_eng)

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val


class Bot2():
	def __init__(self):

		self.min_val, self.max_val = 1, 360
		self.size_getter_eng = 50
		self.create_pos_bot(0, 500, 500)
		self.create_gen_bot()
		self.create_gen_bot()
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)
		self.ge_pos = (0, 0, 0, 0)
		self.counter_angs = 0

	def create_gen_bot(self):
		self.l1, self.l2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.w1, self.w2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.s1, self.s2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.a1, self.a2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.hp, self.eng = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.max_iter_rotate = randint(self.min_val, self.max_val)

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2,
						 self.w1, self.w2,
						 self.s1, self.s2,
						 self.a1, self.a2,
						 self.hp, self.eng,
						 self.max_iter_rotate]

	def create_pos_bot(self, min_x, max_x, y):
		self.pos = (randint(min_x, max_x), y)

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.size_getter_eng / 2, self.pos[
			1] - self.l1 - self.l2 - self.size_getter_eng / 2, self.size_getter_eng, self.size_getter_eng
		return x1, y1, w, h

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		self.re_save_get_eng(ge)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg, master, color_l1, color_l2, color_eng):
		ang1 = self.edit_ang_l1()
		ang2 = self.edit_ang_l2()
		l1 = self.move_l1(ang1)
		l2 = self.move_l2(ang2)
		ge = self.move_getter_eng()
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def edit_ang_l1(self):
		if self.counter_angs < self.max_iter_rotate:
			self.a1 += 1
		if self.counter_angs >= self.max_iter_rotate:
			self.a1 -= 1
		if self.counter_angs >= self.max_iter_rotate * 3:
			self.counter_angs = 0
		# print(self.a1)
		self.counter_angs += 1
		return self.a1

	def edit_ang_l2(self):
		# if 180 < self.a2 < 360:
		self.a2 -= 1
		return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def re_save_get_eng(self, ge):
		self.ge_pos = (ge[0], ge[1], ge[2], ge[3])

	def move_l1(self, ang):
		x1, y1 = self.pos[0], self.pos[1]
		x2 = x1 + cos(radians(ang)) * self.l1
		y2 = y1 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_getter_eng(self):
		self.re_save_get_eng((self.l2_pos[2], self.l2_pos[3], self.size_getter_eng, self.size_getter_eng))
		return (self.l2_pos[2], self.l2_pos[3], self.size_getter_eng, self.size_getter_eng)

	def check_getter_energy(self, array_pos_energy):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				return coords[0], coords[1]
		return None, None

	def check_getter_energy_view(self, array_pos_energy, pg_module, master):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			pg_module.draw.rect(master, (250, 0, 250), (coords[0], coords[1], 10, 10))
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				return coords[0],coords[1]
		return None,None

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val


class Bot3():
	def __init__(self):
		self.min_val, self.max_val = 1, 360
		self.size_getter_eng = 50
		self.create_pos_bot(100, 500, 50)
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)
		self.ge_pos = (0, 0, 0, 0)
		self.counter_angs = 0

	def create_gen_bot(self):
		self.l1, self.l2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.w1, self.w2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.s1, self.s2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.a1, self.a2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.hp, self.eng = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.max_iter_rotate = randint(self.min_val, self.max_val)

	def set_gen_bot(self, arg):
		self.l1, self.l2 ,self.w1, self.w2 ,self.s1, self.s2 ,self.a1, self.a2 ,self.hp, self.eng ,self.max_iter_rotate = arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9], arg[10]
		self.create_arr_gen_bot()

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2,
						 self.w1, self.w2,
						 self.s1, self.s2,
						 self.a1, self.a2,
						 self.hp, self.eng,
						 self.max_iter_rotate]

	def set_gen_code(self, array_gen_code):
		self.arr_gens = array_gen_code
		self.set_gen_bot(array_gen_code)

	def get_gen_code(self):
		return self.arr_gens

	def mutation_gen_code(self):
		random_gen_index = randint(0,len(self.arr_gens)-1)
		random_value_for_gen = randint(self.min_val,self.max_val)
		self.arr_gens[random_gen_index] = random_value_for_gen
		return self.arr_gens

	def create_pos_bot(self, min_x, max_x, y):
		self.pos = (randint(min_x, max_x), y)

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.size_getter_eng / 2, self.pos[
			1] - self.l1 - self.l2 - self.size_getter_eng / 2, self.size_getter_eng, self.size_getter_eng
		return x1, y1, w, h

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		self.re_save_get_eng(ge)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg, master, color_l1, color_l2, color_eng):
		ang1 = self.edit_ang_l1()
		ang2 = self.edit_ang_l2()
		l1 = self.move_l1(ang1)
		l2 = self.move_l2(ang2)
		ge = self.move_getter_eng()
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)
		self.down_hp(1)
		self.down_eng(1)

	def edit_ang_l1(self):
		if self.counter_angs < self.max_iter_rotate:
			self.a1 += 1
		if self.counter_angs >= self.max_iter_rotate:
			self.a1 -= 1
		if self.counter_angs >= self.max_iter_rotate * 3:
			self.counter_angs = 0
		# print(self.a1)
		self.counter_angs += 1
		return self.a1

	def edit_ang_l2(self):
		# if 180 < self.a2 < 360:
		self.a2 -= 1
		return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def re_save_get_eng(self, ge):
		self.ge_pos = (ge[0], ge[1], ge[2], ge[3])

	def move_l1(self, ang):
		x1, y1 = self.pos[0], self.pos[1]
		x2 = x1 + cos(radians(ang)) * self.l1
		y2 = y1 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_getter_eng(self):
		self.re_save_get_eng((self.l2_pos[2], self.l2_pos[3], self.size_getter_eng, self.size_getter_eng))
		return (self.l2_pos[2], self.l2_pos[3], self.size_getter_eng, self.size_getter_eng)

	def check_life(self):
		if self.hp <= 0:
			return False
		else:
			return True


	def check_getter_energy(self, array_pos_energy):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				return coords[0], coords[1]
		return None, None

	def check_getter_energy_view(self, array_pos_energy, pg_module, master):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			pg_module.draw.rect(master, (250, 0, 250), (coords[0], coords[1], 10, 10))
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0],coords[1]
		return None,None

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val

	def up_hp(self,val):
		self.hp += val


class Bot4():
	def __init__(self):
		self.min_val, self.max_val = 1, 360
		self.min_val_l,self.max_val_l = 1, 100
		self.size_getter_eng = 20
		self.create_pos_bot(100, 1000, 100, 600)
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)
		self.ge_pos = (0, 0, 0, 0)
		self.counter_angs = 0

	def create_gen_bot(self):
		self.l1, self.l2 = randint(self.min_val_l, self.max_val_l), randint(self.min_val_l, self.max_val_l)
		self.w1, self.w2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.s1, self.s2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.a1, self.a2 = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.hp, self.eng = randint(self.min_val, self.max_val), randint(self.min_val, self.max_val)
		self.max_iter_rotate = randint(self.min_val, self.max_val)

	def set_gen_bot(self, arg):
		self.l1, self.l2 ,self.w1, self.w2 ,self.s1, self.s2 ,self.a1, self.a2 ,self.hp, self.eng ,self.max_iter_rotate = arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9], arg[10]
		self.create_arr_gen_bot()

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2,
						 self.w1, self.w2,
						 self.s1, self.s2,
						 self.a1, self.a2,
						 self.hp, self.eng,
						 self.max_iter_rotate]

	def set_gen_code(self, array_gen_code):
		self.arr_gens = array_gen_code
		self.set_gen_bot(array_gen_code)

	def get_gen_code(self):
		return self.arr_gens

	def gen_canon_select(self):
		random_gen_index = randint(0,len(self.arr_gens)-1)
		if random_gen_index == 0:
			random_value_for_gen = randint(self.min_val_l,self.max_val_l)
		else:
			random_value_for_gen = randint(self.min_val, self.max_val)
		self.arr_gens[random_gen_index] = random_value_for_gen

	def mutation_gen_code(self):
		random_gen_index = self.gen_canon_select()
		return self.arr_gens

	def create_pos_bot(self, min_x, max_x, min_y, max_y):
		self.pos = (randint(min_x, max_x),(randint(min_y, max_y)))

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.size_getter_eng / 2, self.pos[
			1] - self.l1 - self.l2 - self.size_getter_eng / 2, self.size_getter_eng, self.size_getter_eng
		return x1, y1, w, h

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		self.re_save_get_eng(ge)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg, master, color_l1, color_l2, color_eng):
		if self.check_life():
			ang1 = self.edit_ang_l1()
			ang2 = self.edit_ang_l2()
			l1 = self.move_l1(ang1)
			l2 = self.move_l2(ang2)
			ge = self.move_getter_eng()
			module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
			module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
			module_pg.draw.rect(master, color_eng, ge)
			self.down_hp(0.5)
			self.down_eng(0.5)

	def edit_ang_l1(self):
		if self.counter_angs < self.max_iter_rotate:
			self.a1 += 1
		if self.counter_angs >= self.max_iter_rotate:
			self.a1 -= 1
		if self.counter_angs >= self.max_iter_rotate * 3:
			self.counter_angs = 0
		# print(self.a1)
		self.counter_angs += 1
		return self.a1

	def edit_ang_l2(self):
		# if 180 < self.a2 < 360:
		self.a2 -= 1
		return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def re_save_get_eng(self, ge):
		self.ge_pos = (ge[0], ge[1], ge[2], ge[3])

	def move_l1(self, ang):
		x1, y1 = self.pos[0], self.pos[1]
		x2 = x1 + cos(radians(ang)) * self.l1
		y2 = y1 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_getter_eng(self):
		self.re_save_get_eng((self.l2_pos[2], self.l2_pos[3], self.size_getter_eng, self.size_getter_eng))
		return (self.l2_pos[2], self.l2_pos[3], self.size_getter_eng, self.size_getter_eng)

	def check_life(self):
		if self.hp <= 0:
			return False
		else:
			return True


	def check_getter_energy(self, array_pos_energy):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				return coords[0], coords[1]
		return None, None

	def check_getter_energy_view(self, array_pos_energy, pg_module, master):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			pg_module.draw.rect(master, (250, 0, 250), (coords[0], coords[1], 10, 10))
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0],coords[1]
		return None,None

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val

	def up_hp(self,val):
		self.hp += val


class Bot5():
	def __init__(self):
		self.PERCENT_MUTAGEN = 50  # 5%
		self.DOWN_HP = 1
		self.DOWN_ENG = 0.5
		self.min_val, self.max_val = 1, 360
		self.min_val_l,self.max_val_l = 1, 200
		self.min_val_x1, self.max_val_x1 = 100, 700
		self.min_val_y1, self.max_val_y1 = 100, 700
		self.min_val_x2, self.max_val_x2 = 100, 700
		self.min_val_y2, self.max_val_y2 = 100, 700
		self.min_val_ang1, self.max_val_ang1 = -360, 360 * 2
		self.min_val_ang2, self.max_val_ang2 = -360, 360 * 2
		self.min_val_hp, self.max_val_hp = 10,100
		self.min_val_eng, self.max_val_eng = 10,100
		self.min_val_size_getter_eng, self.max_size_getter_eng = 1,30
		self.min_val_iter_rotate, self.max_val_iter_rotate = -100,100
		self.min_val_step_a1, self.max_val_step_a1 = -5,5
		self.min_val_step_a2, self.max_val_step_a2 = -5,5
		self.create_pos_bot(100, 1000, 100, 600)
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)
		self.ge_pos = (0, 0, 0, 0)
		self.counter_angs = 0

	def create_gen_bot(self):
		self.l1, self.l2 = randint(self.min_val_l, self.max_val_l), randint(self.min_val_l, self.max_val_l)
		self.x1, self.y1 = randint(self.min_val_x1, self.max_val_x1), randint(self.min_val_y1, self.max_val_y1)
		self.x2, self.y2 = randint(self.min_val_x2, self.max_val_x2), randint(self.min_val_y2, self.max_val_y2)
		self.a1, self.a2 = randint(self.min_val_ang1, self.max_val_ang1), randint(self.min_val_ang2, self.max_val_ang2)
		self.hp, self.eng = randint(self.min_val_hp, int(self.max_val_hp/2)), randint(self.min_val_eng, int(self.min_val_eng))
		self.max_iter_rotate = randint(self.min_val_iter_rotate, self.max_val_iter_rotate)
		self.sge = randint(self.min_val_size_getter_eng, self.max_size_getter_eng)
		self.step_a1 = randint(self.min_val_step_a1,self.max_val_step_a1)
		self.step_a2 = randint(self.min_val_step_a2, self.max_val_step_a2)

	def set_gen_bot(self, arg):
		self.l1, self.l2 ,self.x1, self.y1 ,self.x2, self.y2 ,self.a1, self.a2 ,self.hp, self.eng ,self.max_iter_rotate, self.sge, self.step_a1, self.step_a2=\
		arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9], arg[10], arg[11], arg[12], arg[13]
		self.create_arr_gen_bot()

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2,
						 self.x1, self.y1,
						 self.y2, self.y2,
						 self.a1, self.a2,
						 self.hp, self.eng,
						 self.max_iter_rotate,
						 self.sge, self.step_a1, self.step_a2]

	def set_gen_code(self, array_gen_code):
		self.arr_gens = array_gen_code
		self.set_gen_bot(array_gen_code)

	def get_gen_code(self):
		return self.arr_gens

	def gen_canon_select(self):
		percent = randint(0,100)
		if percent in [x for x in range(self.PERCENT_MUTAGEN)]:
			random_gen_index = randint(0,len(self.arr_gens)-1)
			if random_gen_index in [0]:
				random_value_for_gen = randint(self.min_val_l,self.max_val_l)
			elif random_gen_index in [1]:
				random_value_for_gen = randint(self.min_val_l,self.max_val_l)
			elif random_gen_index in [2,3]:
				random_value_for_gen = randint(self.min_val_x1,self.max_val_y1)
			elif random_gen_index in [4,5]:
				random_value_for_gen = randint(self.min_val_x2,self.max_val_y2)
			elif random_gen_index in [6,7]:
				random_value_for_gen = randint(self.min_val_ang1,self.max_val_ang2)
			elif random_gen_index in [8]:
				random_value_for_gen = randint(self.min_val_hp,self.max_val_hp)
			# elif random_gen_index in [9]:
			#     random_value_for_gen = randint(self.min_val_eng,self.max_val_eng)
			elif random_gen_index in [11]:
				random_value_for_gen = randint(self.min_val_size_getter_eng,self.max_size_getter_eng)
			elif random_gen_index in [12]:
				random_value_for_gen = randint(self.min_val_step_a1,self.max_val_step_a1)
			elif random_gen_index in [13]:
				random_value_for_gen = randint(self.min_val_step_a2,self.max_val_step_a2)
			else:
				random_value_for_gen = self.arr_gens[random_gen_index]
			self.arr_gens[random_gen_index] = random_value_for_gen

	def mutation_gen_code(self):
		self.gen_canon_select()
		return self.arr_gens

	def create_pos_bot(self, min_x, max_x, min_y, max_y):
		self.pos = (randint(min_x, max_x),(randint(min_y, max_y)))

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.sge / 2, self.pos[
			1] - self.l1 - self.l2 - self.sge / 2, self.sge, self.sge
		return x1, y1, w, h

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		self.re_save_get_eng(ge)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg, master, color_l1, color_l2, color_eng):
		if self.check_life():
			ang1 = self.edit_ang_l1()
			ang2 = self.edit_ang_l2()
			l1 = self.move_l1(ang1)
			l2 = self.move_l2(ang2)
			ge = self.move_getter_eng()
			module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
			module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
			module_pg.draw.rect(master, color_eng, ge)
			self.down_hp(self.DOWN_HP)
			self.down_eng(self.DOWN_ENG)

	def edit_ang_l1(self):
		print(f"""self.counter_angs [{self.counter_angs}] : self.max_iter_rotate [{self.max_iter_rotate}]""")
		if self.counter_angs < self.max_iter_rotate:
			self.a1 += self.step_a1
			# self.a2 += self.step_a2
		if self.counter_angs >= self.max_iter_rotate:
			# self.a1 -= self.step_a1
			self.a2 -= self.step_a2
			self.counter_angs = randint(0,360)

		# # print(self.a1)
		self.counter_angs += 1

		return self.a1

	def edit_ang_l2(self):

		# print(self.a1)
		# self.counter_angs2 += 1
		return self.a2



		# # if 180 < self.a2 < 360:
		# self.a2 -= 1
		# return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def re_save_get_eng(self, ge):
		self.ge_pos = (ge[0], ge[1], ge[2], ge[3])

	def move_l1(self, ang):
		x1, y1 = self.pos[0], self.pos[1]
		x2 = x1 + cos(radians(ang)) * self.l1
		y2 = y1 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_getter_eng(self):
		self.re_save_get_eng((self.l2_pos[2], self.l2_pos[3], self.sge, self.sge))
		return (self.l2_pos[2], self.l2_pos[3], self.sge, self.sge)

	def check_life(self):
		if self.hp <= 0  or self.eng <= 0:
			return False
		else:
			return True


	def check_getter_energy(self, array_pos_energy):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0], coords[1]
		return None, None

	def check_getter_energy_view(self, array_pos_energy, pg_module, master):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			pg_module.draw.rect(master, (250, 0, 250), (coords[0], coords[1], 10, 10))
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0],coords[1]
		return None,None

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val

	def up_hp(self,val):
		self.hp += val


class BotOptimal():
	def __init__(self):
		self.PERCENT_MUTAGEN = 10  # 5%
		self.DOWN_HP = 1
		self.DOWN_ENG = 0
		self.min_val, self.max_val = 1, 360
		self.min_val_l,self.max_val_l = 1, 150
		self.min_val_x1, self.max_val_x1 = 100, 700
		self.min_val_y1, self.max_val_y1 = 100, 700
		self.min_val_x2, self.max_val_x2 = 100, 700
		self.min_val_y2, self.max_val_y2 = 100, 700
		self.min_val_ang1, self.max_val_ang1 = -360, 360 * 2
		self.min_val_ang2, self.max_val_ang2 = -360, 360 * 2
		self.min_val_hp, self.max_val_hp = 1,100
		self.min_val_eng, self.max_val_eng = 10,100
		self.min_val_size_getter_eng, self.max_size_getter_eng = 1,25
		self.min_val_iter_rotate, self.max_val_iter_rotate = -360,360
		self.min_val_step_a1, self.max_val_step_a1 = -15,15
		self.min_val_step_a2, self.max_val_step_a2 = -15,15
		self.create_pos_bot(100, 1000, 100, 600)
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)
		self.ge_pos = (0, 0, 0, 0)
		self.counter_angs = 0

	def create_gen_bot(self):
		self.l1, self.l2 = randint(self.min_val_l, self.max_val_l), randint(self.min_val_l, self.max_val_l)
		self.x1, self.y1 = randint(self.min_val_x1, self.max_val_x1), randint(self.min_val_y1, self.max_val_y1)
		self.x2, self.y2 = randint(self.min_val_x2, self.max_val_x2), randint(self.min_val_y2, self.max_val_y2)
		self.a1, self.a2 = randint(self.min_val_ang1, self.max_val_ang1), randint(self.min_val_ang2, self.max_val_ang2)
		self.hp, self.eng = randint(self.min_val_hp, int(self.max_val_hp/2)), randint(self.min_val_eng, int(self.min_val_eng))
		self.max_iter_rotate = randint(self.min_val_iter_rotate, self.max_val_iter_rotate)
		self.sge = randint(self.min_val_size_getter_eng, self.max_size_getter_eng)
		self.step_a1 = randint(self.min_val_step_a1,self.max_val_step_a1)
		self.step_a2 = randint(self.min_val_step_a2, self.max_val_step_a2)

	def set_gen_bot(self, arg):
		self.l1, self.l2 ,self.x1, self.y1 ,self.x2, self.y2 ,self.a1, self.a2 ,self.hp, self.eng ,self.max_iter_rotate, self.sge, self.step_a1, self.step_a2=\
		arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9], arg[10], arg[11], arg[12], arg[13]
		self.create_arr_gen_bot()

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2,
						 self.x1, self.y1,
						 self.y2, self.y2,
						 self.a1, self.a2,
						 self.hp, self.eng,
						 self.max_iter_rotate,
						 self.sge, self.step_a1, self.step_a2]

	def set_gen_code(self, array_gen_code):
		self.arr_gens = array_gen_code
		self.set_gen_bot(array_gen_code)

	def get_gen_code(self):
		return self.arr_gens

	def gen_canon_select(self):
		percent = randint(0,100)
		if percent in [x for x in range(self.PERCENT_MUTAGEN)]:
			random_gen_index = randint(0,len(self.arr_gens)-1)
			if random_gen_index in [0]:
				random_value_for_gen = randint(self.min_val_l,self.max_val_l)
			elif random_gen_index in [1]:
				random_value_for_gen = randint(self.min_val_l,self.max_val_l)
			elif random_gen_index in [2,3]:
				random_value_for_gen = randint(self.min_val_x1,self.max_val_y1)
			elif random_gen_index in [4,5]:
				random_value_for_gen = randint(self.min_val_x2,self.max_val_y2)
			elif random_gen_index in [6,7]:
				random_value_for_gen = randint(self.min_val_ang1,self.max_val_ang2)
			elif random_gen_index in [8]:
				random_value_for_gen = randint(self.min_val_hp,self.max_val_hp)
			# elif random_gen_index in [9]:
			#     random_value_for_gen = randint(self.min_val_eng,self.max_val_eng)
			elif random_gen_index in [11]:
				random_value_for_gen = randint(self.min_val_size_getter_eng,self.max_size_getter_eng)
			elif random_gen_index in [12]:
				random_value_for_gen = randint(self.min_val_step_a1,self.max_val_step_a1)
			elif random_gen_index in [13]:
				random_value_for_gen = randint(self.min_val_step_a2,self.max_val_step_a2)
			else:
				random_value_for_gen = self.arr_gens[random_gen_index]
			self.arr_gens[random_gen_index] = random_value_for_gen

	def mutation_gen_code(self):
		self.gen_canon_select()
		return self.arr_gens

	def create_pos_bot(self, min_x, max_x, min_y, max_y):
		self.pos = (randint(min_x, max_x),(randint(min_y, max_y)))

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.sge / 2, self.pos[
			1] - self.l1 - self.l2 - self.sge / 2, self.sge, self.sge
		return x1, y1, w, h

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		self.re_save_get_eng(ge)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg=None, master=None, color_l1=None, color_l2=None, color_eng=None, canvas=None):
		if canvas == None:
			if self.check_life():
				ang1 = self.edit_ang_l1()
				ang2 = self.edit_ang_l2()
				l1 = self.move_l1(ang1)
				l2 = self.move_l2(ang2)
				ge = self.move_getter_eng()
				module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
				module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
				module_pg.draw.rect(master, color_eng, ge)
				self.down_hp(self.DOWN_HP)
				# self.down_eng(self.DOWN_ENG)
		else:
			if self.check_life():
				ang1 = self.edit_ang_l1()
				ang2 = self.edit_ang_l2()
				l1 = self.move_l1(ang1)
				l2 = self.move_l2(ang2)
				ge = self.move_getter_eng()
				canvas.create_line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
				canvas.create_line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
				canvas.create_rectangle(master, color_eng, ge)
				self.down_hp(self.DOWN_HP)
				# self.down_eng(self.DOWN_ENG)

	def edit_ang_l1(self):
		# print(f"""self.counter_angs [{self.counter_angs}] : self.max_iter_rotate [{self.max_iter_rotate}]""")
		if self.counter_angs < self.max_iter_rotate:
			self.a1 += self.step_a1
			# self.a2 += self.step_a2
		if self.counter_angs >= self.max_iter_rotate:
			# self.a1 -= self.step_a1
			self.a2 -= self.step_a2
			self.counter_angs = randint(0,360)

		# # print(self.a1)
		self.counter_angs += 1

		return self.a1

	def edit_ang_l2(self):

		# print(self.a1)
		# self.counter_angs2 += 1
		return self.a2



		# # if 180 < self.a2 < 360:
		# self.a2 -= 1
		# return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def re_save_get_eng(self, ge):
		self.ge_pos = (ge[0], ge[1], ge[2], ge[3])

	def move_l1(self, ang):
		x1, y1 = self.pos[0], self.pos[1]
		x2 = x1 + cos(radians(ang)) * self.l1
		y2 = y1 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_getter_eng(self):
		self.re_save_get_eng((self.l2_pos[2], self.l2_pos[3], self.sge, self.sge))
		return (self.l2_pos[2], self.l2_pos[3], self.sge, self.sge)

	def check_life(self):
		if self.hp <= 0  or self.eng <= 0:
			return False
		else:
			return True


	def check_getter_energy(self, array_pos_energy):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0], coords[1]
		return None, None

	def check_getter_energy_view(self, array_pos_energy, pg_module, master):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			pg_module.draw.rect(master, (250, 0, 250), (coords[0], coords[1], 10, 10))
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0],coords[1]
		return None,None

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val

	def up_hp(self,val):
		self.hp += val


class Bot7():
	def __init__(self):
		self.PERCENT_MUTAGEN = 10  # 5%
		self.DOWN_HP = 1
		self.DOWN_ENG = 0
		self.min_val, self.max_val = 1, 360
		self.min_val_l,self.max_val_l = 1, 70
		self.min_val_x1, self.max_val_x1 = 100, 700
		self.min_val_y1, self.max_val_y1 = 100, 700
		self.min_val_x2, self.max_val_x2 = 100, 700
		self.min_val_y2, self.max_val_y2 = 100, 700
		self.min_val_x3, self.max_val_x3 = 100, 700
		self.min_val_y3, self.max_val_y3 = 100, 700
		self.min_val_ang1, self.max_val_ang1 = -360, 360 * 2
		self.min_val_ang2, self.max_val_ang2 = -360, 360 * 2
		self.min_val_ang3, self.max_val_ang3 = -360, 360 * 2
		self.min_val_hp, self.max_val_hp = 1,100
		self.min_val_eng, self.max_val_eng = 10,100
		self.min_val_size_getter_eng, self.max_size_getter_eng = 1,25
		self.min_val_iter_rotate, self.max_val_iter_rotate = -360,360
		self.min_val_step_a1, self.max_val_step_a1 = -15,15
		self.min_val_step_a2, self.max_val_step_a2 = -15,15
		self.min_val_step_a3, self.max_val_step_a3 = -15, 15
		self.create_pos_bot(100, 1000, 100, 600)
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)
		self.l3_pos = (0, 0, 0, 0)
		self.ge_pos = (0, 0, 0, 0)
		self.counter_angs = 0

	def create_gen_bot(self):
		self.l1, self.l2, self.l3 = randint(self.min_val_l, self.max_val_l), randint(self.min_val_l, self.max_val_l), randint(self.min_val_l, self.max_val_l)
		self.x1, self.y1 = randint(self.min_val_x1, self.max_val_x1), randint(self.min_val_y1, self.max_val_y1)
		self.x2, self.y2 = randint(self.min_val_x2, self.max_val_x2), randint(self.min_val_y2, self.max_val_y2)
		self.x3, self.y3 = randint(self.min_val_x3, self.max_val_x3), randint(self.min_val_y3, self.max_val_y3)
		self.a1, self.a2, self.a3 = randint(self.min_val_ang1, self.max_val_ang1), randint(self.min_val_ang2, self.max_val_ang2), randint(self.min_val_ang3, self.max_val_ang3)
		self.hp, self.eng = randint(self.min_val_hp, int(self.max_val_hp/2)), randint(self.min_val_eng, int(self.min_val_eng))
		self.max_iter_rotate = randint(self.min_val_iter_rotate, self.max_val_iter_rotate)
		self.sge = randint(self.min_val_size_getter_eng, self.max_size_getter_eng)
		self.step_a1 = randint(self.min_val_step_a1,self.max_val_step_a1)
		self.step_a2 = randint(self.min_val_step_a2, self.max_val_step_a2)
		self.step_a3 = randint(self.min_val_step_a3, self.max_val_step_a3)

	def set_gen_bot(self, arg):
		self.l1, self.l2 , self.l3, self.x1, self.y1 ,self.x2, self.y2 , self.x2, self.y3, self.a1, self.a2 , self.a3, self.hp, self.eng ,self.max_iter_rotate, self.sge, self.step_a1, self.step_a2, self.step_a3 =\
		arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9], arg[10], arg[11], arg[12], arg[13], arg[14],arg[15],arg[16],arg[17],arg[18]
		self.create_arr_gen_bot()

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2 , self.l3, self.x1, self.y1 ,self.x2, self.y2 , self.x2, self.y3, self.a1, self.a2 , self.a3, self.hp, self.eng ,self.max_iter_rotate, self.sge, self.step_a1, self.step_a2, self.step_a3]
		# print(self.arr_gens)

	def set_gen_code(self, array_gen_code):
		self.arr_gens = array_gen_code
		self.set_gen_bot(array_gen_code)

	def get_gen_code(self):
		return self.arr_gens

	def gen_canon_select(self):
		percent = randint(0,100)
		if percent in [x for x in range(self.PERCENT_MUTAGEN)]:
			random_gen_index = randint(0,len(self.arr_gens)-1)
			if random_gen_index in [0,1,2]:
				random_value_for_gen = randint(self.min_val_l,self.max_val_l)
			elif random_gen_index in [3]:
				random_value_for_gen = randint(self.min_val_x1,self.max_val_x1)
			elif random_gen_index in [4]:
				random_value_for_gen = randint(self.min_val_y1,self.max_val_y1)
			elif random_gen_index in [5]:
				random_value_for_gen = randint(self.min_val_x2,self.max_val_x2)
			elif random_gen_index in [6]:
				random_value_for_gen = randint(self.min_val_y2,self.max_val_y2)
			elif random_gen_index in [7]:
				random_value_for_gen = randint(self.min_val_x3,self.max_val_y3)
			elif random_gen_index in [8]:
				random_value_for_gen = randint(self.min_val_y3,self.max_val_y3)
			elif random_gen_index in [9]:
				random_value_for_gen = randint(self.min_val_ang1,self.max_val_ang1)
			elif random_gen_index in [10]:
				random_value_for_gen = randint(self.min_val_ang2,self.max_val_ang2)
			elif random_gen_index in [11]:
				random_value_for_gen = randint(self.min_val_ang3,self.max_val_ang3)
			elif random_gen_index in [12]:
				random_value_for_gen = randint(self.min_val_hp,self.max_val_hp)
			# elif random_gen_index in [9]:
			#     random_value_for_gen = randint(self.min_val_eng,self.max_val_eng)
			elif random_gen_index in [14]:
				random_value_for_gen = randint(self.min_val_iter_rotate,self.max_val_iter_rotate)
			elif random_gen_index in [15]:
				random_value_for_gen = randint(self.min_val_size_getter_eng,self.max_size_getter_eng)
			elif random_gen_index in [16]:
				random_value_for_gen = randint(self.min_val_step_a1,self.max_val_step_a1)
			elif random_gen_index in [17]:
				random_value_for_gen = randint(self.min_val_step_a2,self.max_val_step_a2)
			elif random_gen_index in [18]:
				random_value_for_gen = randint(self.min_val_step_a3,self.max_val_step_a3)
			else:
				random_value_for_gen = self.arr_gens[random_gen_index]
			self.arr_gens[random_gen_index] = random_value_for_gen

	def mutation_gen_code(self):
		self.gen_canon_select()
		return self.arr_gens

	def create_pos_bot(self, min_x, max_x, min_y, max_y):
		self.pos = (randint(min_x, max_x),(randint(min_y, max_y)))

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_l3(self):
		x1, y1, x2, y2 = self.pos[0], self.l2_pos[1] - self.l1 - self.l2, self.pos[0], self.pos[1] - self.l1 - self.l2 - self.l3
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.sge / 2, self.pos[
			1] - self.l1 - self.l2 - self.l3 - self.sge / 2, self.sge, self.sge
		return x1, y1, w, h

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_l3, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		l3 = self.create_l3()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		self.re_save_l3(l3)
		self.re_save_get_eng(ge)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.line(master, color_l3, (l3[0], l3[1]), (l3[2], l3[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg, master, color_l1, color_l2, color_l3, color_eng):
		if self.check_life():
			ang1 = self.edit_ang_l1()
			ang2 = self.edit_ang_l2()
			ang3 = self.edit_ang_l3()
			l1 = self.move_l1(ang1)
			l2 = self.move_l2(ang2)
			l3 = self.move_l3(ang3)
			ge = self.move_getter_eng()
			module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
			module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
			module_pg.draw.line(master, color_l3, (l3[0], l3[1]), (l3[2], l3[3]))
			module_pg.draw.rect(master, color_eng, ge)
			self.down_hp(self.DOWN_HP)
			# print(l2,l3)
			# self.down_eng(self.DOWN_ENG)

	def edit_ang_l1(self):
		# print(f"""self.counter_angs [{self.counter_angs}] : self.max_iter_rotate [{self.max_iter_rotate}]""")
		if self.counter_angs < self.max_iter_rotate:
			self.a1 += self.step_a1
			# self.a2 += self.step_a2
		if self.counter_angs >= self.max_iter_rotate:
			# self.a1 -= self.step_a1
			self.a2 -= self.step_a2
			self.counter_angs = randint(0,360)

		# # print(self.a1)
		self.counter_angs += 1

		return self.a1

	def edit_ang_l2(self):

		# print(self.a1)
		# self.counter_angs2 += 1
		return self.a2

	def edit_ang_l3(self):
		# print(self.a1)
		# self.counter_angs2 += 1
		return self.a3



		# # if 180 < self.a2 < 360:
		# self.a2 -= 1
		# return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def re_save_l3(self, l3):
		self.l3_pos = (l3[0], l3[1], l3[2], l3[3])

	def re_save_get_eng(self, ge):
		self.ge_pos = (ge[0], ge[1], ge[2], ge[3])

	def move_l1(self, ang):
		x1, y1 = self.pos[0], self.pos[1]
		x2 = x1 + cos(radians(ang)) * self.l1
		y2 = y1 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l3(self, ang):
		x1, y1 = self.l2_pos[2], self.l2_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l3
		y2 = y1 + sin(radians(ang)) * self.l3
		self.re_save_l3((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_getter_eng(self):
		self.re_save_get_eng((self.l3_pos[2], self.l3_pos[3], self.sge, self.sge))
		return (self.l3_pos[2], self.l3_pos[3], self.sge, self.sge)


	def check_life(self):
		if self.hp <= 0  or self.eng <= 0:
			return False
		else:
			return True


	def check_getter_energy(self, array_pos_energy):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0], coords[1]
		return None, None

	def check_getter_energy_view(self, array_pos_energy, pg_module, master):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			pg_module.draw.rect(master, (250, 0, 250), (coords[0], coords[1], 10, 10))
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0],coords[1]
		return None,None

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val

	def up_hp(self,val):
		self.hp += val



class Bot8():
	def __init__(self):
		self.PERCENT_MUTAGEN = 10  # 5%
		self.DOWN_HP = 1
		self.DOWN_ENG = 0
		self.min_val, self.max_val = 1, 360
		self.min_val_l,self.max_val_l = 1, 150
		self.min_val_x1, self.max_val_x1 = 100, 700
		self.min_val_y1, self.max_val_y1 = 100, 700
		self.min_val_x2, self.max_val_x2 = 100, 700
		self.min_val_y2, self.max_val_y2 = 100, 700
		self.min_val_ang1, self.max_val_ang1 = -360, 360 * 2
		self.min_val_ang2, self.max_val_ang2 = -360, 360 * 2
		self.min_val_hp, self.max_val_hp = 1,100
		self.min_val_eng, self.max_val_eng = 10,100
		self.min_val_size_getter_eng, self.max_size_getter_eng = 1,25
		self.min_val_iter_rotate, self.max_val_iter_rotate = -360,360
		self.min_val_step_a1, self.max_val_step_a1 = -15,15
		self.min_val_step_a2, self.max_val_step_a2 = -15,15
		self.create_pos_bot(100, 1000, 100, 600)
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)
		self.ge_pos = (0, 0, 0, 0)
		self.counter_angs = 0

	def create_gen_bot(self):
		self.l1, self.l2 = randint(self.min_val_l, self.max_val_l), randint(self.min_val_l, self.max_val_l)
		self.x1, self.y1 = randint(self.min_val_x1, self.max_val_x1), randint(self.min_val_y1, self.max_val_y1)
		self.x2, self.y2 = randint(self.min_val_x2, self.max_val_x2), randint(self.min_val_y2, self.max_val_y2)
		self.a1, self.a2 = randint(self.min_val_ang1, self.max_val_ang1), randint(self.min_val_ang2, self.max_val_ang2)
		self.hp, self.eng = randint(self.min_val_hp, int(self.max_val_hp/2)), randint(self.min_val_eng, int(self.min_val_eng))
		self.max_iter_rotate = randint(self.min_val_iter_rotate, self.max_val_iter_rotate)
		self.sge = randint(self.min_val_size_getter_eng, self.max_size_getter_eng)
		self.step_a1 = randint(self.min_val_step_a1,self.max_val_step_a1)
		self.step_a2 = randint(self.min_val_step_a2, self.max_val_step_a2)

	def set_gen_bot(self, arg):
		self.l1, self.l2 ,self.x1, self.y1 ,self.x2, self.y2 ,self.a1, self.a2 ,self.hp, self.eng ,self.max_iter_rotate, self.sge, self.step_a1, self.step_a2=\
		arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9], arg[10], arg[11], arg[12], arg[13]
		self.create_arr_gen_bot()

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2,
						 self.x1, self.y1,
						 self.y2, self.y2,
						 self.a1, self.a2,
						 self.hp, self.eng,
						 self.max_iter_rotate,
						 self.sge, self.step_a1, self.step_a2]

	def set_gen_code(self, array_gen_code):
		self.arr_gens = array_gen_code
		self.set_gen_bot(array_gen_code)

	def get_gen_code(self):
		return self.arr_gens

	def gen_canon_select(self):
		percent = randint(0,100)
		if percent in [x for x in range(self.PERCENT_MUTAGEN)]:
			random_gen_index = randint(0,len(self.arr_gens)-1)
			if random_gen_index in [0]:
				random_value_for_gen = randint(self.min_val_l,self.max_val_l)
			elif random_gen_index in [1]:
				random_value_for_gen = randint(self.min_val_l,self.max_val_l)
			elif random_gen_index in [2,3]:
				random_value_for_gen = randint(self.min_val_x1,self.max_val_y1)
			elif random_gen_index in [4,5]:
				random_value_for_gen = randint(self.min_val_x2,self.max_val_y2)
			elif random_gen_index in [6,7]:
				random_value_for_gen = randint(self.min_val_ang1,self.max_val_ang2)
			elif random_gen_index in [8]:
				random_value_for_gen = randint(self.min_val_hp,self.max_val_hp)
			# elif random_gen_index in [9]:
			#     random_value_for_gen = randint(self.min_val_eng,self.max_val_eng)
			elif random_gen_index in [11]:
				random_value_for_gen = randint(self.min_val_size_getter_eng,self.max_size_getter_eng)
			elif random_gen_index in [12]:
				random_value_for_gen = randint(self.min_val_step_a1,self.max_val_step_a1)
			elif random_gen_index in [13]:
				random_value_for_gen = randint(self.min_val_step_a2,self.max_val_step_a2)
			else:
				random_value_for_gen = self.arr_gens[random_gen_index]
			self.arr_gens[random_gen_index] = random_value_for_gen

	def mutation_gen_code(self):
		self.gen_canon_select()
		return self.arr_gens

	def create_pos_bot(self, min_x, max_x, min_y, max_y):
		self.pos = (300,400)   #(randint(min_x, max_x),(randint(min_y, max_y)))

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.sge / 2, self.pos[
			1] - self.l1 - self.l2 - self.sge / 2, self.sge, self.sge
		return x1, y1, w, h

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		self.re_save_get_eng(ge)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg, master, color_l1, color_l2, color_eng):
		if self.check_life():
			ang1 = self.edit_ang_l1()
			ang2 = self.edit_ang_l2()
			l1 = self.move_l1(ang1)
			l2 = self.move_l2(ang2)
			ge = self.move_getter_eng()
			module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
			module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
			module_pg.draw.rect(master, color_eng, ge)
			self.down_hp(self.DOWN_HP)
			# self.down_eng(self.DOWN_ENG)

	def edit_ang_l1(self):
		# print(f"""self.counter_angs [{self.counter_angs}] : self.max_iter_rotate [{self.max_iter_rotate}]""")
		if self.counter_angs < self.max_iter_rotate:
			self.a1 += self.step_a1
			# self.a2 += self.step_a2
		if self.counter_angs >= self.max_iter_rotate:
			# self.a1 -= self.step_a1
			self.a2 -= self.step_a2
			self.counter_angs = randint(0,360)

		# # print(self.a1)
		self.counter_angs += 1

		return self.a1

	def edit_ang_l2(self):
		if self.counter_angs < self.max_iter_rotate:
			self.a2 += self.step_a2
			# self.a2 += self.step_a2
		if self.counter_angs >= self.max_iter_rotate:
			# self.a1 -= self.step_a1
			self.a1 -= self.step_a1
			self.counter_angs = randint(0,360)
		# print(self.a1)
		# self.counter_angs2 += 1
		return self.a2

	def edit_ang2_l2(self):
		if self.counter_angs < self.max_iter_rotate:
			self.a2 += self.step_a2
			# self.a2 += self.step_a2
		if self.counter_angs >= self.max_iter_rotate:
			# self.a1 -= self.step_a1
			self.a1 -= self.step_a1
			self.counter_angs = randint(0, 360)
		# print(self.a1)
		# self.counter_angs2 += 1
		return self.a2

		# # if 180 < self.a2 < 360:
		# self.a2 -= 1
		# return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def re_save_get_eng(self, ge):
		self.ge_pos = (ge[0], ge[1], ge[2], ge[3])

	def move_l1(self, ang):
		x2, y2 = self.pos[0], self.pos[1]
		x1 = x2 + cos(radians(ang)) * self.l1
		y1 = y2 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2


	def GET_X(self):
		return self.l1_pos[2]

	def move_getter_eng(self):
		self.re_save_get_eng((self.l2_pos[2], self.l2_pos[3], self.sge, self.sge))
		return (self.l2_pos[2], self.l2_pos[3], self.sge, self.sge)

	def check_life(self):
		if self.hp <= 0  or self.eng <= 0:
			return False
		else:
			return True


	def check_getter_energy(self, array_pos_energy):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0], coords[1]
		return None, None

	def check_getter_energy_view(self, array_pos_energy, pg_module, master):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			pg_module.draw.rect(master, (250, 0, 250), (coords[0], coords[1], 10, 10))
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0],coords[1]
		return None,None

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val

	def up_hp(self,val):
		self.hp += val


class Bot9():
	def __init__(self):
		self.PERCENT_MUTAGEN = 50  # 5%
		self.DOWN_HP = 1
		self.DOWN_ENG = 0
		self.min_val, self.max_val = 1, 360
		self.min_val_l,self.max_val_l = 50, 100
		self.min_val_x1, self.max_val_x1 = 100, 700
		self.min_val_y1, self.max_val_y1 = 100, 700
		self.min_val_x2, self.max_val_x2 = 100, 700
		self.min_val_y2, self.max_val_y2 = 100, 700
		self.min_val_x3, self.max_val_x3 = 100, 700
		self.min_val_y3, self.max_val_y3 = 100, 700
		self.min_val_ang1, self.max_val_ang1 = -360, 360 * 2
		self.min_val_ang2, self.max_val_ang2 = -360, 360 * 2
		self.min_val_ang3, self.max_val_ang3 = -360, 360 * 2
		self.min_val_hp, self.max_val_hp = 1,100
		self.min_val_eng, self.max_val_eng = 10,100
		self.min_val_size_getter_eng, self.max_size_getter_eng = 1,25
		self.min_val_iter_rotate, self.max_val_iter_rotate = -360,360
		self.min_val_step_a1, self.max_val_step_a1 = -15,15
		self.min_val_step_a2, self.max_val_step_a2 = -15,15
		self.min_val_step_a3, self.max_val_step_a3 = -15, 15
		self.create_pos_bot(0, 0, 0, 0)
		self.l1_pos = (0, 0, 0, 0)
		self.l2_pos = (0, 0, 0, 0)
		self.l3_pos = (0, 0, 0, 0)
		self.ge_pos = (0, 0, 0, 0)
		self.counter_angs = 0
		self.create_gen_bot()

	def create_gen_bot(self):
		self.l1, self.l2, self.l3 = randint(self.min_val_l, self.max_val_l), randint(self.min_val_l, self.max_val_l), randint(self.min_val_l, self.max_val_l)
		self.x1, self.y1 = randint(self.min_val_x1, self.max_val_x1), randint(self.min_val_y1, self.max_val_y1)
		self.x2, self.y2 = randint(self.min_val_x2, self.max_val_x2), randint(self.min_val_y2, self.max_val_y2)
		self.x3, self.y3 = randint(self.min_val_x3, self.max_val_x3), randint(self.min_val_y3, self.max_val_y3)
		self.a1, self.a2, self.a3 = randint(self.min_val_ang1, self.max_val_ang1), randint(self.min_val_ang2, self.max_val_ang2), randint(self.min_val_ang3, self.max_val_ang3)
		self.hp, self.eng = randint(self.min_val_hp, int(self.max_val_hp/2)), randint(self.min_val_eng, int(self.min_val_eng))
		self.max_iter_rotate = randint(self.min_val_iter_rotate, self.max_val_iter_rotate)
		self.sge = randint(self.min_val_size_getter_eng, self.max_size_getter_eng)
		self.step_a1 = randint(self.min_val_step_a1,self.max_val_step_a1)
		self.step_a2 = randint(self.min_val_step_a2, self.max_val_step_a2)
		self.step_a3 = randint(self.min_val_step_a3, self.max_val_step_a3)

	def set_gen_bot(self, arg):
		self.l1, self.l2 , self.l3, self.x1, self.y1 ,self.x2, self.y2 , self.x2, self.y3, self.a1, self.a2 , self.a3, self.hp, self.eng ,self.max_iter_rotate, self.sge, self.step_a1, self.step_a2, self.step_a3 =\
		arg[0], arg[1], arg[2], arg[3], arg[4], arg[5], arg[6], arg[7], arg[8], arg[9], arg[10], arg[11], arg[12], arg[13], arg[14],arg[15],arg[16],arg[17],arg[18]
		self.create_arr_gen_bot()

	def create_arr_gen_bot(self):
		self.arr_gens = [self.l1, self.l2 , self.l3, self.x1, self.y1 ,self.x2, self.y2 , self.x2, self.y3, self.a1, self.a2 , self.a3, self.hp, self.eng ,self.max_iter_rotate, self.sge, self.step_a1, self.step_a2, self.step_a3]
		# print(self.arr_gens)

	def set_gen_code(self, array_gen_code):
		self.arr_gens = array_gen_code
		self.set_gen_bot(array_gen_code)

	def get_gen_code(self):
		return self.arr_gens

	def gen_canon_select(self):
		percent = randint(0,100)
		if percent in [x for x in range(self.PERCENT_MUTAGEN)]:
			random_gen_index = randint(0,len(self.arr_gens)-1)
			if random_gen_index in [0,1,2]:
				random_value_for_gen = randint(self.min_val_l,self.max_val_l)
			elif random_gen_index in [3]:
				random_value_for_gen = randint(self.min_val_x1,self.max_val_x1)
			elif random_gen_index in [4]:
				random_value_for_gen = randint(self.min_val_y1,self.max_val_y1)
			elif random_gen_index in [5]:
				random_value_for_gen = randint(self.min_val_x2,self.max_val_x2)
			elif random_gen_index in [6]:
				random_value_for_gen = randint(self.min_val_y2,self.max_val_y2)
			elif random_gen_index in [7]:
				random_value_for_gen = randint(self.min_val_x3,self.max_val_y3)
			elif random_gen_index in [8]:
				random_value_for_gen = randint(self.min_val_y3,self.max_val_y3)
			elif random_gen_index in [9]:
				random_value_for_gen = randint(self.min_val_ang1,self.max_val_ang1)
			elif random_gen_index in [10]:
				random_value_for_gen = randint(self.min_val_ang2,self.max_val_ang2)
			elif random_gen_index in [11]:
				random_value_for_gen = randint(self.min_val_ang3,self.max_val_ang3)
			elif random_gen_index in [12]:
				random_value_for_gen = randint(self.min_val_hp,self.max_val_hp)
			# elif random_gen_index in [9]:
			#     random_value_for_gen = randint(self.min_val_eng,self.max_val_eng)
			elif random_gen_index in [14]:
				random_value_for_gen = randint(self.min_val_iter_rotate,self.max_val_iter_rotate)
			elif random_gen_index in [15]:
				random_value_for_gen = randint(self.min_val_size_getter_eng,self.max_size_getter_eng)
			elif random_gen_index in [16]:
				random_value_for_gen = randint(self.min_val_step_a1,self.max_val_step_a1)
			elif random_gen_index in [17]:
				random_value_for_gen = randint(self.min_val_step_a2,self.max_val_step_a2)
			elif random_gen_index in [18]:
				random_value_for_gen = randint(self.min_val_step_a3,self.max_val_step_a3)
			else:
				random_value_for_gen = self.arr_gens[random_gen_index]
			self.arr_gens[random_gen_index] = random_value_for_gen

	def mutation_gen_code(self):
		self.gen_canon_select()
		return self.arr_gens

	def create_pos_bot(self, min_x, max_x, min_y, max_y):
		self.pos = (200, 400)#(randint(min_x, max_x),(randint(min_y, max_y)))

	def create_l1(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[0], self.pos[1] - self.l1
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def create_l2(self):
		x1, y1, x2, y2 = self.pos[0], self.pos[1] - self.l1, self.pos[0], self.pos[1] - self.l1 - self.l2
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_l3(self):
		x1, y1, x2, y2 = self.pos[0], self.l2_pos[1] - self.l1 - self.l2, self.pos[0], self.pos[1] - self.l1 - self.l2 - self.l3
		# print('L2 ',x1, y1, x2, y2)
		return x1, y1, x2, y2

	def create_getter_eng(self):
		x1, y1, w, h = self.pos[0] - self.sge / 2, self.pos[
			1] - self.l1 - self.l2 - self.l3 - self.sge / 2, self.sge, self.sge
		return x1, y1, w, h

	def GET_X(self):
		# print(self.l1_pos)
		return self.l1_pos

	def draw_rect(self, module_pg, master, color_l1, color_l2, color_l3, color_eng):
		l1 = self.create_l1()
		l2 = self.create_l2()
		l3 = self.create_l3()
		ge = self.create_getter_eng()
		self.re_save_l1(l1)
		self.re_save_l2(l2)
		self.re_save_l3(l3)
		self.re_save_get_eng(ge)
		module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
		module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
		module_pg.draw.line(master, color_l3, (l3[0], l3[1]), (l3[2], l3[3]))
		module_pg.draw.rect(master, color_eng, ge)

	def draw_re_move(self, module_pg, master, color_l1, color_l2, color_l3, color_eng):
		if self.check_life():
			ang1 = self.edit_ang_l1()
			ang2 = self.edit_ang_l2()
			ang3 = self.edit_ang_l3()
			l1 = self.move_l1(ang1)
			l2 = self.move_l2(ang2)
			l3 = self.move_l3(ang3)
			ge = self.move_getter_eng()
			module_pg.draw.line(master, color_l1, (l1[0], l1[1]), (l1[2], l1[3]))
			module_pg.draw.line(master, color_l2, (l2[0], l2[1]), (l2[2], l2[3]))
			module_pg.draw.line(master, color_l3, (l3[0], l3[1]), (l3[2], l3[3]))
			module_pg.draw.rect(master, color_eng, ge)
			self.down_hp(self.DOWN_HP)
			# print(l2,l3)
			# self.down_eng(self.DOWN_ENG)

	def edit_ang_l1(self):
		# print(f"""self.counter_angs [{self.counter_angs}] : self.max_iter_rotate [{self.max_iter_rotate}]""")
		if self.counter_angs < self.max_iter_rotate:
			self.a1 += self.step_a1
			# self.a2 += self.step_a2
		if self.counter_angs >= self.max_iter_rotate:
			# self.a1 -= self.step_a1
			self.a2 -= self.step_a2
			self.counter_angs = randint(0,360)

		# # print(self.a1)
		self.counter_angs += 1

		return self.a1

	def edit_ang_l2(self):

		# print(self.a1)
		# self.counter_angs2 += 1
		return self.a2

	def edit_ang_l3(self):
		# print(self.a1)
		# self.counter_angs2 += 1
		return self.a3



		# # if 180 < self.a2 < 360:
		# self.a2 -= 1
		# return self.a2

	def re_save_l1(self, l1):
		self.l1_pos = (l1[0], l1[1], l1[2], l1[3])

	def re_save_l2(self, l2):
		self.l2_pos = (l2[0], l2[1], l2[2], l2[3])

	def re_save_l3(self, l3):
		self.l3_pos = (l3[0], l3[1], l3[2], l3[3])

	def re_save_get_eng(self, ge):
		self.ge_pos = (ge[0], ge[1], ge[2], ge[3])

	def move_l1(self, ang):
		x2, y2 = self.pos[0], self.pos[1]
		x1 = x2 + cos(radians(ang)) * self.l1
		y1 = y2 + sin(radians(ang)) * self.l1
		self.re_save_l1((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l2(self, ang):
		x1, y1 = self.l1_pos[2], self.l1_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l2
		y2 = y1 + sin(radians(ang)) * self.l2
		self.re_save_l2((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_l3(self, ang):
		x1, y1 = self.l2_pos[2], self.l2_pos[3]
		x2 = x1 + cos(radians(ang)) * self.l3
		y2 = y1 + sin(radians(ang)) * self.l3
		self.re_save_l3((x1, y1, x2, y2))
		# print('L1  ', x1,y1,x2,y2)
		return x1, y1, x2, y2

	def move_getter_eng(self):
		self.re_save_get_eng((self.l3_pos[2], self.l3_pos[3], self.sge, self.sge))
		return (self.l3_pos[2], self.l3_pos[3], self.sge, self.sge)


	def check_life(self):
		if self.hp <= 0  or self.eng <= 0:
			return False
		else:
			return True


	def check_getter_energy(self, array_pos_energy):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0], coords[1]
		return None, None

	def check_getter_energy_view(self, array_pos_energy, pg_module, master):
		gx, gy, gw, gh = self.ge_pos[0], self.ge_pos[1], self.ge_pos[2], self.ge_pos[3]
		gx, gy, gw, gh = int(gx), int(gy), int(gw), int(gh)
		for coords in array_pos_energy:  # [x,y] - coords energy
			pg_module.draw.rect(master, (250, 0, 250), (coords[0], coords[1], 10, 10))
			# print(gx, coords[0], gx + gw, gy, coords[1], gy, gh)
			if gx <= coords[0] <= gx + gw and gy <= coords[1] <= gy + gh:
				# print('check' + '_' * 50 + '\n')
				self.up_eng(10)
				self.up_hp(10)
				return coords[0],coords[1]
		return None,None

	def down_hp(self, val):
		self.hp -= val

	def down_eng(self, val):
		self.eng -= val

	def up_eng(self, val):
		self.eng += val

	def up_hp(self,val):
		self.hp += val


