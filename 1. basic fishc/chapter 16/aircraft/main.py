

    font_over = pg.font.Font("font/font.TTF", 48)


    image_resume1 = pg.image.load("image/resume_nor.png").convert_alpha()
    image_resume2 = pg.image.load("image/resume_pressed.png").convert_alpha()



    image_life = pg.image.load("image/life.png").convert_alpha()
    rect_life = image_life.get_rect()


    rect_pause_resume = image_pause1.get_rect()


    image_again = pg.image.load("image/again.png").convert_alpha()
    rect_again = image_again.get_rect()

    image_over = pg.image.load("image/gameover.png").convert_alpha()
    rect_over = image_over.get_rect()

    pg.mixer_music.load("sound/game_music.ogg")
    pg.mixer_music.set_volume(0.2)

    sound_upgrade = pg.mixer.Sound("sound/upgrade.wav")
    sound_bomb_use = pg.mixer.Sound("sound/use_bomb.wav")
    sound_bomb_get = pg.mixer.Sound("sound/get_bomb.wav")
    sound_supply = pg.mixer.Sound("sound/supply.wav")
    sound_bullet_get = pg.mixer.Sound("sound/get_bullet.wav")

    # 再处理会变的东西
    player = Player(screen, SPEED_PLAYER, FRAME_SPRITE)

    # 设置all的目的是便于同一进行碰撞检测等, 不然得来三遍
    group_enemy_all = pg.sprite.Group()
    group_enemy_small = pg.sprite.Group()
    group_enemy_mid = pg.sprite.Group()
    group_enemy_big = pg.sprite.Group()

    # 子弹是有顺序的, 所以不能用group
    group_bullet1 = list()

    group_bullet2 = list()

    supply_bomb = BombSupply(screen)
    supply_bullet = BulletSupply(screen)


    def add_small_enemy(num):
        for i in range(num):
            enemy = SmallEnemy(screen, SPEED_ENEMY_SMALL, HEALTH_ENEMY_SMALL)
            group_enemy_small.add(enemy)
            group_enemy_all.add(enemy)

    def add_mid_enemy(num):
        for i in range(num):
            enemy = MidEnemy(screen, SPEED_ENEMY_MID, HEALTH_ENEMY_MID)
            group_enemy_mid.add(enemy)
            group_enemy_all.add(enemy)


    def add_big_enemy(num):
        for i in range(num):
            enemy = BigEnemy(screen, SPEED_ENEMY_BIG, HEALTH_ENEMY_BIG, FRAME_SPRITE)
            group_enemy_big.add(enemy)
            group_enemy_all.add(enemy)

    def add_bullet1(num):
        for i in range(num):
            bullet = Bullet1(player, SPEED_BULLET1)
            group_bullet1.append(bullet)

    def add_bullet2(num):
        for i in range(num):
            # 超级子弹需要指定是哪侧的
            bullet = Bullet2(player, SPEED_BULLET2, 'left')
            group_bullet2.append(bullet)
            bullet = Bullet2(player, SPEED_BULLET2, 'right')
            group_bullet2.append(bullet)

    # 各各级别并不是把所有敌机速度都加1, 可能只加小的或中的
    def increase_speed(target, inc):
        for each in target:
            each.speed += inc

    # 定义各阶段的初始化函数 LAUNCH, PLAY, PAUSE, TERMINATE
    # 由于初始化函数还要初始化一些基本类型变量, 这些变量记得用nonlocal
    # 或者用一个字典或者类存这些变量


    class rt:
        image_pause_resume = image_pause1
        index_frame = 0
        score = 0
        best_score = 0
        level = 1
        num_bomb = NUM_BOMB
        # 设想一种情况, 吃到双倍子弹, 用了5秒, 暂停, 再回来, 应该还能继续用13秒
        # 用set_timer实现不了这个效果, 不如找个字段直接存当前双倍剩余时间以及基准时间
        # 吃到新的子弹补给更新剩余时长和基准时间
        # 每一帧判断, 如果当前tick-tick_base超过了剩余时间, 那么剩余时间置为0
        # 如果点了暂停, 判断还有没有剩余时间, 如果有, 存下来还剩多少
        # 由暂停再回来的时候, 更新基准时间
        bullet_double = 0
        tick_base = 0

        num_player = 3

        group_bullet = group_bullet1

    def initialize(stage_to, stage_from):


        if stage_to == PLAY:

            rt.image_pause_resume = image_pause1
            rect_pause_resume.x = WIDTH - rect_pause_resume.width - 10
            rect_pause_resume.top = 10

            rect_bomb.x = 10
            rect_bomb.y = HEIGHT-rect_bomb.height-10

            # 重置发放补给的计时器, 每30秒发一次
            pg.time.set_timer(TIMER_SUPPLY, 0)  # 为防止其他场景没终止计时器, 这里终止一下
            pg.time.set_timer(TIMER_SUPPLY, 5*1000)

            #  不是从暂停过来的, 重置所有游戏状态
            if stage_from == LAUNCH:
                # -1表示无限重复
                pg.mixer_music.play(-1)
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                add_bullet1(NUM_BULLET1)
                add_bullet2(NUM_BULLET2)

                rt.index_frame = 0
                rt.score = 0
                rt.level = 1
                rt.num_bomb = NUM_BOMB
                rt.bullet_double = 0
                rt.tick_base = 0
                rt.num_player = 3
                rt.group_bullet = group_bullet1

            elif stage_from == PAUSE:
                pg.mixer_music.unpause()
                rt.tick_base = pg.time.get_ticks()
            else:
                # 为了防止从其他需要重新开始的地方来的时候背景音乐还在继续
                # 这里强制终止背景音乐
                pg.mixer_music.stop()
                pg.mixer_music.play(-1)

                # 重置玩家飞机
                player.reset()

                # 重置敌机, 注意group的数量可能超过了初始数量
                group_enemy_all.empty()
                group_enemy_small.empty()
                group_enemy_mid.empty()
                group_enemy_big.empty()

                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)

                rt.index_frame = 0
                rt.score = 0
                rt.level = 1
                rt.num_bomb = NUM_BOMB
                rt.num_player = 3

        elif stage_to == PAUSE:
            # 到PAUSE的只可能来源于PLAY, 所以不用判断from
            rt.image_pause_resume = image_resume1
            pg.time.set_timer(TIMER_SUPPLY, 0)

            if rt.bullet_double:
                rt.bullet_double -= pg.time.get_ticks()-rt.tick_base
        else:
            pg.time.set_timer(TIMER_SUPPLY, 0)
            pg.mixer_music.stop()
            pg.mixer.stop()
            if os.path.isfile("record.txt"):
                with open("record.txt", "r") as f:
                    rt.best_score = int(f.read())
            if rt.score > rt.best_score:
                rt.best_score = rt.score
                with open("record.txt", "w") as f:
                    f.write(str(rt.score))
            rt.text_best_score = font_score.render("Best: {}".format(rt.best_score), True, WHITE)
            rt.rect_best_score = rt.text_best_score.get_rect()
            rt.rect_best_score.topleft = (20, 20)

            rt.text_yourscore = font_over.render("Your Score", True, WHITE)
            rt.rect_yourscore = rt.text_yourscore.get_rect()
            rt.rect_yourscore.midtop = screen.get_rect().midtop
            rt.rect_yourscore.top+=HEIGHT//3

            rt.text_score = font_over.render(str(rt.score), True, WHITE)
            rt.rect_score = rt.text_score.get_rect()
            rt.rect_score.midtop = screen.get_rect().midtop
            rt.rect_score.top += rt.rect_yourscore.bottom+10

            rect_again.midtop = rt.rect_score.midbottom
            rect_again.top += 20

            rect_over.midtop = rect_again.midbottom
            rect_over.top += 10




    stage = PLAY
    initialize(stage, LAUNCH)

    clock = pg.time.Clock()

    # 一些简单的页面要素就别去创建精灵类了, 直接在主函数里画

    while True:

        event = pg.event.get()
        for e in event:
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()

        if stage == PLAY:
            # 响应用户键盘操作有两种方法, 一是通过KEYDOWN和KEYUP事件
            # 另一种是调用key模块的get_pressed()方法
            # 第一种仅适用于偶尔触发的键盘事件, 所以这里用第二种
            keys = pg.key.get_pressed()
            # 注意这里没用else, 所以同时按下两个键是支持的
            if keys[K_w] or keys[K_UP]: player.moveUp()
            if keys[K_s] or keys[K_DOWN]: player.moveDown()
            if keys[K_a] or keys[K_LEFT]: player.moveLeft()
            if keys[K_d] or keys[K_RIGHT]: player.moveRight()

            # 这里炸弹不能用第二种键盘事件方式
            # 第二种无法区分一次按下, 比如快速按一下空格, 可能接下来的几次
            # 循环, 都会识别空格是按下的
            for e in event:
                if e.type == KEYDOWN and e.key == K_SPACE:
                    if rt.num_bomb:
                        rt.num_bomb -= 1
                        sound_bomb_use.play()
                        for each in group_enemy_all:
                            if each.active:
                                each.active = 0
                                if each in group_enemy_small:
                                    rt.score += 1000
                                if each in group_enemy_mid:
                                    rt.score += 6000
                                if each in group_enemy_big:
                                    rt.score += 10000
                if e.type == TIMER_SUPPLY:
                    sound_supply.play()

                    if random.choice([True, False]):
                        supply_bomb.release()
                    else:
                        supply_bullet.release()



            screen.blit(player.image, player.rect)

            for i in range(rt.num_player):
                rect_life.bottom = HEIGHT - 10
                rect_life.right = WIDTH - 10 - i * rect_life.width
                screen.blit(image_life, rect_life)

            # 这里除了每隔一定帧去发射子弹, 也可以通过设置set_timer
            # 每隔一段时间给一个该发射子弹的信号
            if rt.index_frame % FRAME_BULLET == 0:
                # 非双倍时间
                if not rt.bullet_double:
                    bullet = rt.group_bullet.pop(0)
                    rt.group_bullet.append(bullet)
                    bullet.fire()
                else:
                    # 双倍子弹, 一次回收俩, 不管其状态
                    bullet = rt.group_bullet.pop(0)
                    rt.group_bullet.append(bullet)
                    bullet.fire()
                    bullet = rt.group_bullet.pop(0)
                    rt.group_bullet.append(bullet)
                    bullet.fire()

            rt.index_frame += 1
            # 子弹只能这么画, 没办法用group统一处理
            for each in rt.group_bullet:
                if each.active: screen.blit(each.image, each.rect)

            group_enemy_all.draw(screen)

            if rt.bullet_double:
                if pg.time.get_ticks()-rt.tick_base >= rt.bullet_double:
                    rt.bullet_double = 0
                    for each in group_bullet1:
                        each.active = False
                    rt.group_bullet = group_bullet1

            # 处理补给
            if supply_bomb.active:
                screen.blit(supply_bomb.image, supply_bomb.rect)
                if pg.sprite.collide_mask(player, supply_bomb):
                    sound_bomb_get.play()
                    if rt.num_bomb < 3: rt.num_bomb += 1
                    supply_bomb.active = False
                else:
                    supply_bomb.move()

            if supply_bullet.active:
                screen.blit(supply_bullet.image, supply_bullet.rect)
                if pg.sprite.collide_mask(player, supply_bullet):
                    sound_bullet_get.play()

                    rt.bullet_double = TIME_DOUBLE_BULLET
                    rt.tick_base = pg.time.get_ticks()

                    for each in group_bullet2:
                        each.active = False
                    rt.group_bullet = group_bullet2

                    supply_bullet.active = False
                else:
                    supply_bullet.move()

            # 处理子弹碰撞
            for each in rt.group_bullet:
                # 注意状态不对的子弹不要去判断碰撞
                if not each.active: continue
                # 每一颗正常状态的子弹去判断是否和敌机有碰撞, 以及是否y小于0
                collides = pg.sprite.spritecollide(each, group_enemy_all, False, pg.sprite.collide_mask)
                if each.y < 0 or collides:
                    each.active = False  # 重新进入弹药库, 注意不能无限制地生成新的子弹, 内存会慢慢受不了的

                for enemy in collides:
                    if enemy.active:
                        enemy.energy -= 1
                        enemy.hit = True
                        if enemy.energy == 0:
                            enemy.active = False
                            if enemy in group_enemy_small:
                                rt.score += 1000
                            if enemy in group_enemy_mid:
                                rt.score += 6000
                            if enemy in group_enemy_big:
                                rt.score += 10000

                # 击中之后, 下一帧, 如果没击中, 就要把hit字段改回来, 取消显示击中图片
                for each in group_enemy_mid:
                    if each not in collides:
                        each.hit = False
                for each in group_enemy_big:
                    if each not in collides:
                        each.hit = False

            # 中大飞机的三种状态都画血条就行了
            for each in group_enemy_mid: each.showHealth()
            for each in group_enemy_big: each.showHealth()


            # 再处理飞机碰撞
            if not player.invincible:
                collides = pg.sprite.spritecollide(player, group_enemy_all, False,
                                                   pg.sprite.collide_mask)
                if collides:
                    # 这里要判断, 非破坏状态下才能再次赋值破坏状态
                    # 因为破坏状态下是不检测碰撞的
                    # 如果不判断, 那每次都赋值False, 而active又用的property, 每次都从第一张破坏图开始, 就死那了
                    # 这里之所以要判断active为True的时候才改False而不是无脑改False
                    # 因为播放毁灭生效是放在player和enemy类里写了
                    if player.active:
                        player.active = False

                    for item in collides:
                        if item.active: item.active = False

            player.update()
            for each in rt.group_bullet: each.move()

            # 在敌机下一次移动之前, 根据分数判断是否升级
            if rt.level == 1 and rt.score >= 50000:
                rt.level = 2
                sound_upgrade.play()
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                increase_speed(group_enemy_small, SPEED_INC)
            elif rt.level == 2 and rt.score >= 300000:
                rt.level = 3
                sound_upgrade.play()
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                increase_speed(group_enemy_small, SPEED_INC)
                increase_speed(group_enemy_mid, SPEED_INC)
            elif rt.level == 3 and rt.score >= 600000:
                rt.level = 4
                sound_upgrade.play()
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                increase_speed(group_enemy_small, SPEED_INC)
                increase_speed(group_enemy_mid, SPEED_INC)
            elif rt.level == 4 and rt.score >= 1000000:
                rt.level = 5
                sound_upgrade.play()
                add_small_enemy(NUM_ENEMY_SMALL)
                add_mid_enemy(NUM_ENEMY_MID)
                add_big_enemy(NUM_ENEMY_BIG)
                increase_speed(group_enemy_small, SPEED_INC)
                increase_speed(group_enemy_mid, SPEED_INC)

            group_enemy_all.update()

            # 暂停按钮为什么要放后面, 因为改了状态后不希望继续执行下面的代码了
            for e in event:
                
                if e.type == EVENT_PLAYER_DESTROYED:
                    if rt.num_player > 1:
                        player.reset()
                        rt.num_player -= 1
                        player.invincible = True
                        pg.time.set_timer(TIMER_INVINCIBLE, 3*1000)
                    else:
                        stage = TERMINATE
                        initialize(stage, PLAY)
                        break
                if e.type == TIMER_INVINCIBLE:
                    player.invincible = False

        elif stage == PAUSE:
            # 暂停状态所有要素都画, 只不过不更新
            screen.blit(image_background, (0, 0))
            screen.blit(player.image, player.rect)
            for each in rt.group_bullet:
                if each.active: screen.blit(each.image, each.rect)
            group_enemy_all.draw(screen)
            for each in group_enemy_mid: each.showHealth()
            for each in group_enemy_big: each.showHealth()
            text_score = font_score.render("Score: {}".format(rt.score), True, WHITE)
            screen.blit(text_score, (10, 5))

            # 下角画炸弹
            text_bomb = font_bomb.render("x {}".format(rt.num_bomb), True, WHITE)
            rect_bomb_text = text_bomb.get_rect()
            rect_bomb_text.x = rect_bomb.right+10
            rect_bomb_text.y = HEIGHT-rect_bomb_text.height-5
            screen.blit(image_bomb, rect_bomb)
            screen.blit(text_bomb, rect_bomb_text)


            for i in range(rt.num_player):
                rect_life.bottom = HEIGHT - 10
                rect_life.right = WIDTH - 10 - i * rect_life.width
                screen.blit(image_life, rect_life)

            if supply_bomb.active:
                screen.blit(supply_bomb.image, supply_bomb.rect)

            if supply_bullet.active:
                screen.blit(supply_bullet.image, supply_bullet.rect)

            screen_alpha.fill(WHITE_TRANSPARENT)
            screen_alpha.blit(rt.image_pause_resume, rect_pause_resume)
            screen.blit(screen_alpha, (0, 0))

            for e in event:
                if e.type == MOUSEMOTION and rect_pause_resume.collidepoint(e.pos):
                    rt.image_pause_resume = image_resume2
                else:
                    rt.image_pause_resume = image_resume1

                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if rect_pause_resume.collidepoint(e.pos):
                        stage = PLAY
                        initialize(stage, PAUSE)
                        break

        else:
            screen.blit(image_background, (0, 0))
            screen.blit(rt.text_best_score, rt.rect_best_score)
            screen.blit(rt.text_yourscore, rt.rect_yourscore)
            screen.blit(rt.text_score, rt.rect_score)
            screen.blit(image_again, rect_again)
            screen.blit(image_over, rect_over)

            for e in event:
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if rect_again.collidepoint(e.pos):
                        main()
                        break
                    if rect_over.collidepoint(e.pos):
                        pg.quit()
                        sys.exit()

        pg.display.flip()
        clock.tick(FRAME)

