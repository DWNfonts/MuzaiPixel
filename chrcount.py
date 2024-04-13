from xml.dom.minidom import parse
import xml.dom.minidom

nameIdList = [
    'Copyright notice',
    'Font Family name',
    'Font Subfamily name',
    'Unique font identifier',
    'Full font name',
    'Version string',
    'PostScript name for the font',
    'Trademark',
    'Manufacturer Name',
    'Designer',
    'Description',
    'URL Vendor',
    'URL Designer',
    'License Description',
    'License Info URL',
    '', # Reserved
    'Typographic Family name',
    'Typographic Subfamily name',
    'Compatible Full',
    'Sample text',
    'PostScript CID findfont name',
    'WWS Family Name',
    'WWS Subfamily Name',
    'Light Background Palette',
    'Dark Background Palette',
    'Variations PostScript Name Prefix'
]

通用规范汉字表字表 = [
    "一乙二十丁厂七卜八人入儿匕几九刁了刀力乃又三干于亏工土士才下寸大丈与万上小口山巾千乞川亿个夕久么勺凡丸及广亡门丫义之尸己已巳弓子卫也女刃飞习叉马乡丰王开井天夫元无云专丐扎艺木五支厅不犬太区历歹友尤匹车巨牙屯戈比互切瓦止少曰日中贝冈内水见午牛手气毛壬升夭长仁什片仆化仇币仍仅斤爪反介父从仑今凶分乏公仓月氏勿欠风丹匀乌勾凤六文亢方火为斗忆计订户认冗讥心尺引丑巴孔队办以允予邓劝双书幻玉刊未末示击打巧正扑卉扒功扔去甘世艾古节本术可丙左厉石右布夯戊龙平灭轧东卡北占凸卢业旧帅归旦目且叶甲申叮电号田由只叭史央兄叽叼叫叩叨另叹冉皿凹囚四生矢失乍禾丘付仗代仙们仪白仔他斥瓜乎丛令用甩印尔乐句匆册卯犯外处冬鸟务包饥主市立冯玄闪兰半汁汇头汉宁穴它讨写让礼训议必讯记永司尼民弗弘出辽奶奴召加皮边孕发圣对台矛纠母幼丝邦式迂刑戎动扛寺吉扣考托老巩圾执扩扫地场扬耳芋共芒亚芝朽朴机权过臣吏再协西压厌戌在百有存而页匠夸夺灰达列死成夹夷轨邪尧划迈毕至此贞师尘尖劣光当早吁吐吓虫曲团吕同吊吃因吸吗吆屿屹岁帆回岂则刚网肉年朱先丢廷舌竹迁乔迄伟传乒乓休伍伏优臼伐延仲件任伤价伦份华仰仿伙伪自伊血向似后行舟全会杀合兆企众爷伞创肌肋朵杂危旬旨旭负匈名各多争色壮冲妆冰庄庆亦刘齐交衣次产决亥充妄闭问闯羊并关米灯州汗污江汛池汝汤忙兴宇守宅字安讲讳军讶许讹论讼农讽设访诀寻那迅尽导异弛孙阵阳收阶阴防奸如妇妃好她妈戏羽观欢买红驮纤驯约级纪驰纫巡寿弄麦玖玛形进戒吞远违韧运扶抚坛技坏抠扰扼拒找批址扯走抄贡汞坝攻赤折抓扳抡扮抢孝坎均抑抛投坟坑抗坊抖护壳志块扭声把报拟却抒劫芙芜苇芽花芹芥芬苍芳严芦芯劳克芭苏杆杠杜材村杖杏杉巫极李杨求甫匣更束吾豆两酉丽医辰励否还尬歼来连轩步卤坚肖旱盯呈时吴助县里呆吱吠呕园旷围呀吨足邮男困吵串员呐听吟吩呛吻吹呜吭吧邑吼囤别吮岖岗帐财针钉牡告我乱利秃秀私每兵估体何佐佑但伸佃作伯伶佣低你住位伴身皂伺佛囱近彻役返余希坐谷妥含邻岔肝肛肚肘肠龟甸免狂犹狈角删条彤卵灸岛刨迎饭饮系言冻状亩况床库庇疗吝应这冷庐序辛弃冶忘闰闲间闷判兑灶灿灼弟汪沐沛汰沥沙汽沃沦汹泛沧没沟沪沈沉沁怀忧忱快完宋宏牢究穷灾良证启评补初社祀识诈诉罕诊词译君灵即层屁尿尾迟局改张忌际陆阿陈阻附坠妓妙妖姊妨妒努忍劲矣鸡纬驱纯纱纲纳驳纵纷纸纹纺驴纽奉玩环武青责现玫表规抹卦坷坯拓拢拔坪拣坦担坤押抽拐拖者拍顶拆拎拥抵拘势抱拄垃拉拦幸拌拧拂拙招坡披拨择抬拇拗其取茉苦昔苛若茂苹苗英苟苑苞范直茁茄茎苔茅枉林枝杯枢柜枚析板松枪枫构杭杰述枕丧或画卧事刺枣雨卖郁矾矿码厕奈奔奇奋态欧殴垄妻轰顷转斩轮软到非叔歧肯齿些卓虎虏肾贤尚旺具味果昆国哎咕昌呵畅明易咙昂迪典固忠呻咒咋咐呼鸣咏呢咄咖岸岩帖罗帜帕岭凯败账贩贬购贮图钓制知迭氛垂牧物乖刮秆和季委秉佳侍岳供使例侠侥版侄侦侣侧凭侨佩货侈依卑的迫质欣征往爬彼径所舍金刹命肴斧爸采觅受乳贪念贫忿肤肺肢肿胀朋股肮肪肥服胁周昏鱼兔狐忽狗狞备饰饱饲变京享庞店夜庙府底疟疙疚剂卒郊庚废净盲放刻育氓闸闹郑券卷单炬炒炊炕炎炉沫浅法泄沽河沾泪沮油泊沿泡注泣泞泻泌泳泥沸沼波泼泽治怔怯怖性怕怜怪怡学宝宗定宠宜审宙官空帘宛实试郎诗肩房诚衬衫视祈话诞诡询该详建肃录隶帚屉居届刷屈弧弥弦承孟陋陌孤陕降函限妹姑姐姓妮始姆迢驾叁参艰线练组绅细驶织驹终驻绊驼绍绎经贯契贰奏春帮玷珍玲珊玻毒型拭挂封持拷拱项垮挎城挟挠政赴赵挡拽哉挺括垢拴拾挑垛指垫挣挤拼挖按挥挪拯某甚荆茸革茬荐巷带草茧茵茶荒茫荡荣荤荧故胡荫荔南药标栈柑枯柄栋相查柏栅柳柱柿栏柠树勃要柬咸威歪研砖厘厚砌砂泵砚砍面耐耍牵鸥残殃轴轻鸦皆韭背战点虐临览竖省削尝昧盹是盼眨哇哄哑显冒映星昨咧昭畏趴胃贵界虹虾蚁思蚂虽品咽骂勋哗咱响哈哆咬咳咪哪哟炭峡罚贱贴贻骨幽钙钝钞钟钢钠钥钦钧钩钮卸缸拜看矩毡氢怎牲选适秒香种秋科重复竿段便俩贷顺修俏保促俄俐侮俭俗俘信皇泉鬼侵禹侯追俊盾待徊衍律很须叙剑逃食盆胚胧胆胜胞胖脉胎勉狭狮独狰狡狱狠贸怨急饵饶蚀饺饼峦弯将奖哀亭亮度迹庭疮疯疫疤咨姿亲音帝施闺闻闽阀阁差养美姜叛送类迷籽娄前首逆兹总炼炸烁炮炫烂剃洼洁洪洒柒浇浊洞测洗活派洽染洛浏济洋洲浑浓津恃恒恢恍恬恤恰恼恨举觉宣宦室宫宪突穿窃客诫冠诬语扁袄祖神祝祠误诱诲说诵垦退既屋昼屏屎费陡逊眉孩陨除险院娃姥姨姻娇姚娜怒架贺盈勇怠癸蚤柔垒绑绒结绕骄绘给绚骆络绝绞骇统耕耘耗耙艳泰秦珠班素匿蚕顽盏匪捞栽捕埂捂振载赶起盐捎捍捏埋捉捆捐损袁捌都哲逝捡挫换挽挚热恐捣壶捅埃挨耻耿耽聂恭莽莱莲莫莉荷获晋恶莹莺真框梆桂桔栖档桐株桥桦栓桃格桩校核样根索哥速逗栗贾酌配翅辱唇夏砸砰砾础破原套逐烈殊殉顾轿较顿毙致柴桌虑监紧党逞晒眠晓哮唠鸭晃哺晌剔晕蚌畔蚣蚊蚪蚓哨哩圃哭哦恩鸯唤唁哼唧啊唉唆罢峭峨峰圆峻贼贿赂赃钱钳钻钾铁铃铅缺氧氨特牺造乘敌秤租积秧秩称秘透笔笑笋债借值倚俺倾倒倘俱倡候赁俯倍倦健臭射躬息倔徒徐殷舰舱般航途拿耸爹舀爱豺豹颁颂翁胰脆脂胸胳脏脐胶脑脓逛狸狼卿逢鸵留鸳皱饿馁凌凄恋桨浆衰衷高郭席准座症病疾斋疹疼疲脊效离紊唐瓷资凉站剖竞部旁旅畜阅羞羔瓶拳粉料益兼烤烘烦烧烛烟烙递涛浙涝浦酒涉消涡浩海涂浴浮涣涤流润涧涕浪浸涨烫涩涌悖悟悄悍悔悯悦害宽家宵宴宾窍窄容宰案请朗诸诺读扇诽袜袖袍被祥课冥谁调冤谅谆谈谊剥恳展剧屑弱陵祟陶陷陪娱娟恕娥娘通能难预桑绢绣验继骏球琐理琉琅捧堵措描域捺掩捷排焉掉捶赦堆推埠掀授捻教掏掐掠掂培接掷控探据掘掺职基聆勘聊娶著菱勒黄菲萌萝菌萎菜萄菊菩萍菠萤营乾萧萨菇械彬梦婪梗梧梢梅检梳梯桶梭救曹副票酝酗厢戚硅硕奢盔爽聋袭盛匾雪辅辆颅虚彪雀堂常眶匙晨睁眯眼悬野啪啦曼晦晚啄啡距趾啃跃略蚯蛀蛇唬累鄂唱患啰唾唯啤啥啸崖崎崭逻崔帷崩崇崛婴圈铐铛铝铜铭铲银矫甜秸梨犁秽移笨笼笛笙符第敏做袋悠偿偶偎偷您售停偏躯兜假衅徘徙得衔盘舶船舵斜盒鸽敛悉欲彩领脚脖脯豚脸脱象够逸猜猪猎猫凰猖猛祭馅馆凑减毫烹庶麻庵痊痒痕廊康庸鹿盗章竟商族旋望率阎阐着羚盖眷粘粗粒断剪兽焊焕清添鸿淋涯淹渠渐淑淌混淮淆渊淫渔淘淳液淤淡淀深涮涵婆梁渗情惜惭悼惧惕惟惊惦悴惋惨惯寇寅寄寂宿窒窑密谋谍谎谐袱祷祸谓谚谜逮敢尉屠弹隋堕随蛋隅隆隐婚婶婉颇颈绩绪续骑绰绳维绵绷绸综绽绿缀巢琴琳琢琼斑替揍款堪塔搭堰揩越趁趋超揽堤提博揭喜彭揣插揪搜煮援搀裁搁搓搂搅壹握搔揉斯期欺联葫散惹葬募葛董葡敬葱蒋蒂落韩朝辜葵棒棱棋椰植森焚椅椒棵棍椎棉棚棕棺榔椭惠惑逼粟棘酣酥厨厦硬硝确硫雁殖裂雄颊雳暂雅翘辈悲紫凿辉敞棠赏掌晴睐暑最晰量鼎喷喳晶喇遇喊遏晾景畴践跋跌跑跛遗蛙蛛蜓蜒蛤喝鹃喂喘喉喻啼喧嵌幅帽赋赌赎赐赔黑铸铺链销锁锄锅锈锋锌锐甥掰短智氮毯氯鹅剩稍程稀税筐等筑策筛筒筏答筋筝傲傅牌堡集焦傍储皓皖粤奥街惩御循艇舒逾番释禽腊脾腋腔腕鲁猩猬猾猴惫然馈馋装蛮就敦斌痘痢痪痛童竣阔善翔羡普粪尊奠道遂曾焰港滞湖湘渣渤渺湿温渴溃溅滑湃渝湾渡游滋渲溉愤慌惰愕愣惶愧愉慨割寒富寓窜窝窖窗窘遍雇裕裤裙禅禄谢谣谤谦犀属屡强粥疏隔隙隘媒絮嫂媚婿登缅缆缉缎缓缔缕骗编骚缘瑟鹉瑞瑰瑙魂肆摄摸填搏塌鼓摆携搬摇搞塘摊聘斟蒜勤靴靶鹊蓝墓幕蓬蓄蒲蓉蒙蒸献椿禁楚楷榄想槐榆楼概赖酪酬感碍碘碑碎碰碗碌尴雷零雾雹辐辑输督频龄鉴睛睹睦瞄睫睡睬嗜鄙嗦愚暖盟歇暗暇照畸跨跷跳跺跪路跤跟遣蜈蜗蛾蜂蜕嗅嗡嗓署置罪罩蜀幌错锚锡锣锤锥锦键锯锰矮辞稚稠颓愁筹签简筷毁舅鼠催傻像躲魁衙微愈遥腻腰腥腮腹腺鹏腾腿鲍猿颖触解煞雏馍馏酱禀痹廓痴痰廉靖新韵意誊粮数煎塑慈煤煌满漠滇源滤滥滔溪溜漓滚溢溯滨溶溺粱滩慎誉塞寞窥窟寝谨褂裸福谬群殿辟障媳嫉嫌嫁叠缚缝缠缤剿静碧璃赘熬墙墟嘉摧赫截誓境摘摔撇聚慕暮摹蔓蔑蔡蔗蔽蔼熙蔚兢模槛榴榜榨榕歌遭酵酷酿酸碟碱碳磁愿需辖辗雌裳颗瞅墅嗽踊蜻蜡蝇蜘蝉嘛嘀赚锹锻镀舞舔稳熏箕算箩管箫舆僚僧鼻魄魅貌膜膊膀鲜疑孵馒裹敲豪膏遮腐瘩瘟瘦辣彰竭端旗精粹歉弊熄熔煽潇漆漱漂漫滴漾演漏慢慷寨赛寡察蜜寥谭肇褐褪谱隧嫩翠熊凳骡缩慧撵撕撒撩趣趟撑撮撬播擒墩撞撤增撰聪鞋鞍蕉蕊蔬蕴横槽樱橡樟橄敷豌飘醋醇醉磕磊磅碾震霄霉瞒题暴瞎嘻嘶嘲嘹影踢踏踩踪蝶蝴蝠蝎蝌蝗蝙嘿嘱幢墨镇镐镑靠稽稻黎稿稼箱篓箭篇僵躺僻德艘膝膛鲤鲫熟摩褒瘪瘤瘫凛颜毅糊遵憋潜澎潮潭鲨澳潘澈澜澄懂憔懊憎额翩褥谴鹤憨慰劈履豫缭撼擂操擅燕蕾薯薛薇擎薪薄颠翰噩橱橙橘整融瓢醒霍霎辙冀餐嘴踱蹄蹂蟆螃器噪鹦赠默黔镜赞穆篮篡篷篱儒邀衡膨雕鲸磨瘾瘸凝辨辩糙糖糕燃濒澡激懒憾懈窿壁避缰缴戴擦藉鞠藏藐檬檐檀礁磷霜霞瞭瞧瞬瞳瞩瞪曙蹋蹈螺蟋蟀嚎赡穗魏簧簇繁徽爵朦臊鳄癌辫赢糟糠燥懦豁臀臂翼骤藕鞭藤覆瞻蹦嚣镰翻鳍鹰瀑襟璧戳孽警蘑藻攀曝蹲蹭蹬巅簸簿蟹颤靡癣瓣羹鳖爆疆鬓壤馨耀躁蠕嚼嚷巍籍鳞魔糯灌譬蠢霸露霹躏黯髓赣囊镶瓤罐矗",
    "乂乜兀弋孑孓幺亓韦廿丏卅仄厄仃仉仂兮刈爻卞闩讣尹夬爿毋邗邛艽艿札叵匝丕匜劢卟叱叻仨仕仟仡仫仞卮氐犰刍邝邙汀讦讧讪讫尻阡尕弁驭匡耒玎玑邢圩圬圭扦圪圳圹扪圮圯芊芍芄芨芑芎芗亘厍夼戍尥乩旯曳岌屺凼囡钇缶氘氖牝伎伛伢佤仵伥伧伉伫囟汆刖夙旮刎犷犸舛凫邬饧汕汔汐汲汜汊忖忏讴讵祁讷聿艮厾阱阮阪丞妁牟纡纣纥纨玕玙抟抔圻坂坍坞抃抉㧐芫邯芸芾苈苣芷芮苋芼苌苁芩芪芡芟苄苎苡杌杓杞杈忑孛邴邳矶奁豕忒欤轫迓邶忐卣邺旰呋呒呓呔呖呃旸吡町虬呗吽吣吲帏岐岈岘岑岚兕囵囫钊钋钌迕氙氚牤佞邱攸佚佝佟佗伽彷佘佥孚豸坌肟邸奂劬狄狁鸠邹饨饩饪饫饬亨庑庋疔疖肓闱闳闵羌炀沣沅沔沤沌沏沚汩汨沂汾沨汴汶沆沩泐怃怄忡忤忾怅忻忪怆忭忸诂诃诅诋诌诏诒孜陇陀陂陉妍妩妪妣妊妗妫妞姒妤邵劭刭甬邰纭纰纴纶纾玮玡玭玠玢玥玦盂忝匦坩抨拤坫拈垆抻劼拃拊坼坻㧟坨坭抿坳耶苷苯苤茏苫苜苴苒苘茌苻苓茚茆茑茓茔茕茀苕枥枇杪杳枧杵枨枞枋杻杷杼矸砀刳奄瓯殁郏轭郅鸢盱昊昙杲昃咂呸昕昀旻昉炅咔畀虮咀呷黾呱呤咚咆咛呶呣呦咝岢岿岬岫帙岣峁刿迥岷剀帔峄沓囹罔钍钎钏钒钕钗邾迮牦竺迤佶佬佰侑侉臾岱侗侃侏侩佻佾侪佼佯侬帛阜侔徂刽郄怂籴瓮戗肼䏝肽肱肫剁迩郇狙狎狍狒咎炙枭饯饴冽冼庖疠疝疡兖妾劾炜𬉼炖炘炝炔泔沭泷泸泱泅泗泠泺泖泫泮沱泯泓泾怙怵怦怛怏怍㤘怩怫怿宕穹宓诓诔诖诘戾诙戽郓衩祆祎祉祇诛诜诟诠诣诤诧诨诩戕孢亟陔妲妯姗帑弩孥驽虱迦迨绀绁绂驷驸绉绌驿骀甾珏珐珂珑玳珀顸珉珈拮垭挝垣挞垤赳贲垱垌郝垧垓挦垠茜荚荑贳荜莒茼茴茱莛荞茯荏荇荃荟荀茗荠茭茨垩荥荦荨荩剋荪茹荬荮柰栉柯柘栊柩枰栌柙枵柚枳柞柝栀柢栎枸柈柁枷柽剌酊郦甭砗砘砒斫砭砜奎耷虺殂殇殄殆轱轲轳轶轸虿毖觇尜哐眄眍𠳐郢眇眊眈禺哂咴曷昴昱昵咦哓哔畎毗呲胄畋畈虼虻盅咣哕剐郧咻囿咿哌哙哚咯咩咤哝哏哞峙峣罘帧峒峤峋峥贶钚钛钡钣钤钨钫钯氡氟牯郜秕秭竽笈笃俦俨俅俪叟垡牮俣俚皈俑俟逅徇徉舢俞郗俎郤爰郛瓴胨胪胛胂胙胍胗胝朐胫鸨匍狨狯飑狩狲訇逄昝饷饸饹胤孪娈弈奕庥疬疣疥疭庠竑彦飒闼闾闿阂羑迸籼酋炳炻炽炯烀炷烃洱洹洧洌浃洇洄洙涎洎洫浍洮洵浒浔浕洳恸恓恹恫恺恻恂恪恽宥扃衲衽衿袂祛祜祓祚诮祗祢诰诳鸩昶郡咫弭牁胥陛陟娅姮娆姝姣姘姹怼羿炱矜绔骁骅绗绛骈耖挈珥珙顼珰珩珧珣珞琤珲敖恚埔埕埘埙埚挹耆耄埒捋贽垸捃盍荸莆莳莴莪莠莓莜莅荼莩荽莸荻莘莎莞莨鸪莼栲栳郴桓桡桎桢桤梃栝桕桁桧桅栟桉栩逑逋彧鬲豇酐逦厝孬砝砹砺砧砷砟砼砥砣剞砻轼轾辂鸫趸龀鸬虔逍眬唛晟眩眙哧哽唔晁晏鸮趵趿畛蚨蚜蚍蚋蚬蚝蚧唢圄唣唏盎唑崂崃罡罟峪觊赅钰钲钴钵钹钺钽钼钿铀铂铄铆铈铉铊铋铌铍䥽铎氩氤氦毪舐秣秫盉笄笕笊笏笆俸倩俵偌俳俶倬倏恁倭倪俾倜隼隽倌倥臬皋郫倨衄颀徕舫釜奚衾胯胱胴胭脍胼朕脒胺鸱玺鸲狷猁狳猃狺逖桀袅饽凇栾挛亳疳疴疸疽痈疱痂痉衮凋颃恣旆旄旃阃阄訚阆恙粑朔郸烜烨烩烊剡郯烬涑浯涞涟娑涅涠浞涓浥涔浜浠浣浚悚悭悝悒悌悛宸窈剜诹冢诼袒袢祯诿谀谂谄谇屐屙陬勐奘牂蚩陲姬娠娌娉娲娩娴娣娓婀畚逡绠骊绡骋绥绦绨骎邕鸶彗耜焘舂琏琇麸揶埴埯捯掳掴埸埵赧埤捭逵埝堋堍掬鸷掖捽掊堉掸捩掮悫埭埽掇掼聃菁萁菘堇萘萋菽菖萜萸萑棻菔菟萏萃菏菹菪菅菀萦菰菡梵梿梏觋桴桷梓棁桫棂啬郾匮敕豉鄄酞酚戛硎硭硒硖硗硐硇硌鸸瓠匏厩龚殒殓殍赉雩辄堑眭眦啧晡晤眺眵眸圊喏喵啉勖晞唵晗冕啭畦趺啮跄蚶蛄蛎蛆蚰蛊圉蚱蛉蛏蚴啁啕唿啐唼唷啖啵啶啷唳唰啜帻崚崦帼崮崤崆赇赈赊铑铒铗铙铟铠铡铢铣铤铧铨铩铪铫铬铮铯铰铱铳铵铷氪牾鸹秾逶笺筇笸笪笮笠笥笤笳笾笞偾偃偕偈傀偬偻皑皎鸻徜舸舻舴舷龛翎脬脘脲匐猗猡猞猝斛猕馗馃馄鸾孰庹庾痔痍疵翊旌旎袤阇阈阉阊阋阍阏羟粝粕敝焐烯焓烽焖烷焗渍渚淇淅淞渎涿淖挲淠涸渑淦淝淬涪淙涫渌淄惬悻悱惝惘悸惆惚惇惮窕谌谏扈皲谑裆袷裉谒谔谕谖谗谙谛谝逯郿隈粜隍隗婧婊婕娼婢婵胬袈翌恿欸绫骐绮绯绱骒绲骓绶绺绻绾骖缁耠琫琵琶琪瑛琦琥琨靓琰琮琯琬琛琚辇鼋揳堞搽揸揠堙趄揖颉塄揿耋揄蛩蛰塆摒揆掾聒葑葚靰靸葳葺葸萼葆葩葶蒌萱戟葭楮棼椟棹椤棰赍椋椁椪棣椐鹁覃酤酢酡鹂厥殚殛雯雱辊辋椠辍辎斐睄睑睇睃戢喋嗒喃喱喹晷喈跖跗跞跚跎跏跆蛱蛲蛭蛳蛐蛔蛞蛴蛟蛘喁喟啾嗖喑嗟喽嗞喀喔喙嵘嵖崴遄詈嵎崽嵬嵛嵯嵝嵫幄嵋赕铻铼铿锃锂锆锇锉锏锑锒锔锕掣矬氰毳毽犊犄犋鹄犍嵇黍稃稂筚筵筌傣傈舄牍傥傧遑傩遁徨媭畲弑颌翕釉鹆舜貂腈腌腓腆腴腑腚腱鱿鲀鲂颍猢猹猥飓觞觚猱颎飧馇馊亵脔裒痣痨痦痞痤痫痧赓竦瓿啻颏鹇阑阒阕粞遒孳焯焜焙焱鹈湛渫湮湎湜渭湍湫溲湟溆湲湔湉渥湄滁愠惺愦惴愀愎愔喾寐谟扉裢裎裥祾祺谠幂谡谥谧遐孱弼巽骘媪媛婷巯翚皴婺骛缂缃缄彘缇缈缌缑缒缗飨耢瑚瑁瑜瑗瑄瑕遨骜韫髡塬鄢趔趑摅摁蜇搋搪搐搛搠摈彀毂搦搡蓁戡蓍鄞靳蓐蓦鹋蒽蓓蓖蓊蒯蓟蓑蒿蒺蓠蒟蒡蒹蒴蒗蓥颐楔楠楂楝楫楸椴槌楯皙榈槎榉楦楣楹椽裘剽甄酮酰酯酩蜃碛碓硼碉碚碇碜鹌辏龃龅訾粲虞睚嗪韪嗷嗉睨睢雎睥嘟嗑嗫嗬嗔嗝戥嗄煦暄遢暌跬跶跸跐跣跹跻蛸蜊蜍蜉蜣畹蛹嗣嗯嗥嗲嗳嗌嗍嗨嗐嗤嗵罨嵊嵩嵴骰锗锛锜锝锞锟锢锨锩锭锱雉氲犏歃稞稗稔筠筢筮筲筱牒煲敫徭愆艄觎毹貊貅貉颔腠腩腼腭腧塍媵詹鲅鲆鲇鲈稣鲋鲐肄鹐飕觥遛馐鹑亶瘃痱痼痿瘐瘁瘆麂裔歆旒雍阖阗阙羧豢粳猷煳煜煨煅煊煸煺滟溱溘漭滢溥溧溽裟溻溷滗滫溴滏滃滦溏滂滓溟滪愫慑慊鲎骞窦窠窣裱褚裨裾裰禊谩谪媾嫫媲嫒嫔媸缙缜缛辔骝缟缡缢缣骟耥璈瑶瑭獒觏慝嫠韬叆髦摽墁撂摞撄翥踅摭墉墒榖綦蔫蔷靺靼鞅靿甍蔸蔟蔺戬蕖蔻蓿斡鹕蓼榛榧榻榫榭槔榱槁槟槠榷僰酽酶酹厮碡碴碣碲磋臧豨殡霆霁辕蜚裴翡龇龈睿䁖睽嘞嘈嘌嘁嘎暧暝踌踉蜞蜥蜮蝈蜴蜱蜩蜷蜿螂蜢嘘嘡鹗嘣嘤嘚嗾嘧罴罱幔嶂幛赙罂骷骶鹘锲锴锶锷锸锵镁镂犒箐箦箧箍箸箬箅箪箔箜箢箓毓僖儆僳僭劁僮魃魆睾艋鄱膈膑鲑鲔鲚鲛鲟獐觫雒夤馑銮塾麽瘌瘊瘘瘙廖韶旖膂阚鄯鲞粿粼粽糁槊鹚熘熥潢漕滹漯漶潋潴漪漉漳漩澉潍慵搴窨寤綮谮褡褙褓褛褊谯谰谲暨屣鹛嫣嫱嫖嫦嫚嫘嫡鼐翟瞀鹜骠缥缦缧缨骢缪缫耦耧瑾璜璀璎璁璋璇奭髯髫撷撅赭撸鋆撙撺墀聩觐鞑蕙鞒蕈蕨蕤蕞蕺瞢蕃蕲赜槿樯槭樗樘樊槲醌醅靥魇餍磔磙霈辘龉龊觑瞌瞋瞑嘭噎噶颙暹噘踔踝踟踒踬踮踯踺踞蝽蝾蝻蝰蝮螋蝓蝣蝼噗嘬颚噍噢噙噜噌噔颛幞幡嶙嶝骺骼骸镊镉镌镍镏镒镓镔稷箴篑篁篌篆牖儋徵磐虢鹞膘滕鲠鲡鲢鲣鲥鲧鲩獗獠觯馓馔麾廛瘛瘼瘢瘠齑羯羰𥻗遴糌糍糅熜熵熠澍澌潸潦潲鋈潟潼潺憬憧寮窳谳褴褟褫谵熨屦嬉勰戮蝥缬缮缯骣畿耩耨耪璞璟靛璠璘聱螯髻髭髹擀熹甏擞縠磬颞蕻鞘颟薤薨檠薏薮薜薅樾橛橇樵檎橹樽樨橼墼橐翮醛醐醍醚磲赝飙殪霖霏霓錾辚臻遽氅瞟瞠瞰嚄嚆噤暾蹀踹踵踽蹉蹁螨蟒螈螅螭螠螟噱噬噫噻噼罹圜䦃镖镗镘镚镛镝镞镠氇氆憩穑篝篥篦篪篙盥劓翱魉魈徼歙膳膦膙鲮鲱鲲鲳鲴鲵鲷鲻獴獭獬邂鹧廨赟瘰廪瘿瘵瘴癃瘳斓麇麈嬴壅羲糗瞥甑燎燠燔燧濑濉潞澧澹澥澶濂褰寰窸褶禧嬖犟隰嬗颡缱缲缳璨璩璐璪螫擤壕觳罄擢薹鞡鞬薷薰藓藁檄檩懋醢翳礅磴鹩龋龌豳壑黻嚏嚅蹑蹒蹊蟥螬螵疃螳蟑嚓羁罽罾嶷黜黝髁髀镡镢镣镦镧镩镪镫罅黏簌篾篼簖簋鼢黛儡鹪鼾皤魍龠繇貘邈貔臌膻臆臃鲼鲽鳀鳃鳅鳇鳊螽燮鹫襄糜縻膺癍麋懑濡濮濞濠濯蹇謇邃襁檗擘孺隳嬷蟊鹬鍪鏊鳌鬈鬃瞽鞯鞨鞫鞧鞣藜藠藩醪蹙礓燹餮瞿曛颢曜躇蹚鹭蟛蟪蟠蟮鹮黠黟髅髂镬镭镯馥簟簪鼬雠艟鳎鳏鳐癞癔癜癖糨蹩鎏懵彝邋鬏攉攒鞲鞴藿蘧蘅麓醮醯酃霪霭霨黼嚯蹰蹶蹽蹼蹴蹾蹿蠖蠓蟾蠊黢髋髌镲籀籁齁魑艨鳓鳔鳕鳗鳙麒鏖羸㸆瀚瀣瀛襦谶襞骥缵瓒攘蘩蘖醴霰酆矍曦躅鼍巉黩黥黪镳镴黧纂璺鼯臜鳜鳝鳟獾孀骧瓘鼙醺礴颦曩鳢癫麝夔爝灏禳鐾羼蠡耱懿蘸鹳霾氍饕躐髑镵穰饔鬻鬟趱攫攥颧躜鼹癯麟蠲蠹躞衢鑫灞襻纛鬣攮囔馕戆爨齉",
    "亍尢彳卬殳𠙶毌邘戋圢氕伋仝冮氿汈氾忉宄𬣙讱扞圲圫芏芃朳朸𨙸邨吒吖屼屾辿钆仳伣伈癿甪邠犴冱邡闫𬇕汋䜣讻𬣞孖𬘓纩玒玓玘玚刬𫭟坜坉扽𫭢坋扺㧑毐芰芣苊苉芘芴芠𫇭芤杕杙杄杧杩尪尨轪𫐄坒芈旴旵呙㕮岍𫵷岠岜呇冏觃岙伾㑇伭佖伲佁飏狃闶汧汫𣲘𣲗沄沘𬇙汭㳇沇忮忳忺𬣡祃诇邲诎诐屃𫸩岊阽䢺阼妧妘𨚕纮驲𫘜纻𬘘𫘝纼玤玞玱玟邽邿坥坰坬坽弆耵䢼𦭜茋苧苾苠枅㭎枘枍矼矻匼𬨂𬀩𬀪旿昇昄昒昈咉咇咍岵岽岨岞峂㟃囷𬬩钐钔钖牥佴垈侁侹佸佺隹㑊侂佽侘郈舠郐郃攽肭肸肷狉狝饳忞於炌炆泙沺泂泜泃泇怊峃穸祋祊𫍣𬣳𬩽鸤弢弨陑𬮿陎𬯀卺乸妭姈𫰛迳叕𬳵驵𬳶䌹驺𫠊绋绐砉耔㛃玶珇珅𬍛珋玹珌玿韨垚垯垙垲埏垍耇鿍垎垴垟垞挓垵垏拶荖荁荙荛茈茽荄茺𬜬荓茳𦰡茛荭㭕柷柃柊枹栐柖郚剅䴓迺厖砆砑砄耏奓䶮轵轷轹轺昺𪾢昽盷咡咺昳昣哒昤昫昡咥昪虷虸哃峘耑峛𪨰峗峧帡钘𫓧钜𬬮𬬱𬬭钪钬钭矧秬俫舁俜俙俍垕衎舣弇侴鸧䏡胠𦙶胈胩胣朏飐訄饻庤疢炣炟㶲洭洘洓洿㳚泚浈浉洸洑洢洈洚洺洨浐㳘洴洣恔宬窀扂袆祏祐祕叚陧陞娀姞姱姤姶姽枲绖骃𬘡𬳽𬘩𫄧彖骉恝珪珛珹琊玼珖𪟝珽珦珫珒𬍤珢珕珝𫭼埗垾垺埆垿埌埇莰茝𬜯鄀莶莝䓖莙栻桠𬂩桄梠栴梴栒酎酏𫠆砵砠砫砬硁恧翃郪𨐈辀辁𬌗剕赀哢晅晊唝哳哱冔晔晐晖畖蚄蚆𫑡帱崁峿𪨶崄帨崀赆𬬸钷𬬻𬬹𬬿𬭁眚甡笫倻倴脩倮倕倞𫢸倓倧衃虒舭舯舥瓞鬯鸰脎朓胲虓鱽狴峱狻眢𫗧勍痄疰痃竘羖羓桊敉烠烔烶烻𬊈涍浡浭浬涄涢涐浰浟浛浼浲涘悈悃悢𬒈宧窅窊窎扅扆袪袗袯祧隺堲疍𨺙陴烝砮㛚哿翀翂剟𬳿𫄨绤骍𬘫䂮琎珸珵琄琈琀珺掭堎堐埼掎埫堌晢𫮃掞埪壸㙍聍菝萚菥莿䓫勚䓬萆菂菍菼萣䓨菉䓛梼梽桲梾桯梣梌桹敔厣硔鿎硙硚硊硍勔䴕龁逴唪啫翈㫰晙畤𬱖趼跂蛃蚲𬟽蚺啴䎃崧崟崞崒崌崡铏𫓯𫟹铕𫟼铖铘铚铞铥铴牻牿稆笱笯偰偡鸺偭偲偁㿠鄅偓徛衒舳舲鸼悆鄃瓻䝙脶脞脟䏲鱾猇猊猄觖𠅤庱庼庳痓䴔竫堃阌羝羕焆烺焌淏𬇹淟淜淴淯湴涴𬍡㥄惛惔悰惙寁逭𬤇𫍯袼裈祲𬤊𫍲谞艴弸弶𬯎隃婞娵婼媖婳婍婌婫婤婘婠𬘬𬘭𬴂𫘦绹𫟅𬘯骕𫘧絜珷琲琡琟琔琭堾堼揕㙘堧喆堨塅堠絷𪣻𡎚葜惎萳葙靬葴蒇蒈鄚蒉蓇萩蒐葰葎鄑蒎葖蒄萹棤棽棫椓椑𬃊鹀椆棓棬棪椀楗𬷕甦酦觌奡皕硪欹詟𫐐辌棐龂𬹼黹牚睎晫晪晱𧿹蛑畯斝喤崶嵁𫶇崾嵅崿嵚翙𫖮圌圐赑淼赒鿏铹𬭊铽𨱇𫓶锊锍锎𬭎锓犇颋稌筀筘筜筥筅傃傉翛傒傕舾畬𫖯脿腘䐃腙腒𬱟鲃猰𫛭猯㺄馉凓鄗𫷷廋廆鄌粢遆旐𬮱焞𬊤欻𣸣溚溁湝渰湓㴔渟溠渼溇湣湑溞愐愃敩甯棨扊裣祼婻媆媞㛹媓媂媄毵矞𬴃𫘨缊缐骙瑃瑓瑅瑆䴖瑖瑝瑔瑀𤧛瑳瑂嶅瑑遘髢塥堽赪摛塝搒搌蒱蒨蓏蔀蓢蓂蒻蓣椹楪榃榅楒楞楩榇椸楙歅𬪩碃碏𬒔碈䃅硿鄠辒𬨎𫐓龆觜䣘暕鹍𫫇㬊暅跱蜐蜎嵲赗骱锖𫓹锘锳锧锪𬭚锫锬𬭛稑稙䅟𬕂筻筼筶筦筤傺鹎僇艅艉谼貆腽腨腯鲉鲊鲌䲟𬶋𬶍鲏雊猺飔觟𦝼馌裛廒瘀瘅鄘鹒鄜麀鄣阘𫔶煁煃煴煋煟煓滠溍溹滆滉溦溵漷滧滘滍愭慥慆塱𫌀裼禋禔禘禒谫鹔𫖳愍嫄媱戤勠戣𫘪𫘬缞耤瑧𫞩瑨瑱瑷瑢斠摏墕墈墐墘摴銎𡐓墚撖𪤗靽鞁蔌蔈蓰蔹蔊嘏榰榑槚𣗋槜榍疐𬸘酺酾酲酴碶䃎𬒗碨𥔲碹碥劂𫚖䴗夥瞍鹖㬎跽蜾幖嶍圙𨱏锺锼锽𬭤锾锿镃镄镅馝鹙箨箖劄僬僦僔僎槃㙦鲒鲕𫚕鲖鲗鲘鲙𬶐𬶏𩽾夐獍飗𬸚凘廑廙瘗瘥瘕鲝鄫熇漹漖潆漤潩漼漴㽏漈漋漻慬窬窭㮾𬤝褕禛禚隩嫕嫭嫜嫪𬙂㻬麹璆漦叇墣墦墡劐薁蕰蔃鼒槱鹝磏磉殣慭霅暵暲暶踦踣䗖蝘蝲蝤噇噂噀罶嶲嶓㠇嶟嶒镆镈镋镎𬭩镕稹儇皞皛䴘艎艏鹟𩾃鲦鲪鲬橥觭鹠鹡糇糈翦鹢鹣熛潖潵㵐澂澛瑬潽潾潏憭憕𬸣戭褯禤𫍽嫽遹𬴊璥璲璒憙擐鄹薳鞔黇𬞟蕗薢蕹橞橑橦醑觱磡𥕢磜豮𫟦𬺈𫠜鹾虤暿曌曈㬚蹅踶䗛螗疁㠓幪𪩘嶦𬭬𨱑𬭯馞穄篚篯簉鼽衠盦螣縢鲭鲯鲰鲺鲹𫗴亸癀瘭𬸦羱糒燋熻燊燚燏濩濋澪澽澴澭澼憷憺懔黉嬛鹨翯𫄷璱𤩽璬璮髽擿薿薸檑櫆檞醨繄磹磻瞫瞵蹐蟏㘎𬭳镤𬭶𫔍镥镨𬭸𨱔𬭼𫔎矰穙穜穟簕簃簏儦魋斶艚𬸪谿䲠𬶟鲾𬶠鲿鳁鳂鳈鳉獯䗪馘襕襚𬶨螱甓嬬嬥𦈡𫄸瓀釐鬶爇鞳鞮𬟁藟藦藨鹲檫黡礞礌𥖨蹢蹜蟫䗴嚚髃镮镱酂馧簠簝簰鼫鼩皦臑䲢鳑鳒鹱鹯癗𦒍旞翷冁䎖瀔瀍瀌襜䴙𬙊嚭㰀鬷醭蹯蠋翾鳘儳儴鼗𬶭𩾌鳚鳛麑麖蠃彟嬿鬒蘘欂醵颥甗𨟠巇酅髎犨𬶮𨭉㸌爔瀱瀹瀼瀵襫孅骦𬙋耰𤫉瓖鬘趯𬺓罍鼱鳠鳡鳣爟爚灈韂糵蘼礵鹴躔皭龢鳤亹籥鼷𫚭玃醾齇觿蠼"
]

基本集字表 = [
    "啊阿埃挨哎唉哀皑癌蔼矮艾碍爱隘鞍氨安俺按暗岸胺案肮昂盎凹敖熬翱袄傲奥懊澳芭捌扒叭吧笆八疤巴拔跋靶把耙坝霸罢爸白柏百摆佰败拜稗斑班搬扳般颁板版扮拌伴瓣半办绊邦帮梆榜膀绑棒磅蚌镑傍谤苞胞包褒剥薄雹保堡饱宝抱报暴豹鲍爆杯碑悲卑北辈背贝钡倍狈备惫焙被奔苯本笨崩绷甭泵蹦迸逼鼻比鄙笔彼碧蓖蔽毕毙毖币庇痹闭敝弊必辟壁臂避陛鞭边编贬扁便变卞辨辩辫遍标彪膘表鳖憋别瘪彬斌濒滨宾摈兵冰柄丙秉饼炳病并玻菠播拨钵波博勃搏铂箔伯帛舶脖膊渤泊驳捕卜哺补埠不布步簿部怖擦猜裁材才财睬踩采彩菜蔡餐参蚕残惭惨灿苍舱仓沧藏操糙槽曹草厕策侧册测层蹭插叉茬茶查碴搽察岔差诧拆柴豺搀掺蝉馋谗缠铲产阐颤昌猖场尝常长偿肠厂敞畅唱倡超抄钞朝嘲潮巢吵炒车扯撤掣彻澈郴臣辰尘晨忱沉陈趁衬撑称城橙成呈乘程惩澄诚承逞骋秤吃痴持匙池迟弛驰耻齿侈尺赤翅斥炽充冲虫崇宠抽酬畴踌稠愁筹仇绸瞅丑臭初出橱厨躇锄雏滁除楚础储矗搐触处揣川穿椽传船喘串疮窗幢床闯创吹炊捶锤垂春椿醇唇淳纯蠢戳绰疵茨磁雌辞慈瓷词此刺赐次聪葱囱匆从丛凑粗醋簇促蹿篡窜摧崔催脆瘁粹淬翠村存寸磋撮搓措挫错搭达答瘩打大呆歹傣戴带殆代贷袋待逮怠耽担丹单郸掸胆旦氮但惮淡诞弹蛋当挡党荡档刀捣蹈倒岛祷导到稻悼道盗德得的蹬灯登等瞪凳邓堤低滴迪敌笛狄涤翟嫡抵底地蒂第帝弟递缔颠掂滇碘点典靛垫电佃甸店惦奠淀殿碉叼雕凋刁掉吊钓调跌爹碟蝶迭谍叠丁盯叮钉顶鼎锭定订丢东冬董懂动栋侗恫冻洞兜抖斗陡豆逗痘都督毒犊独读堵睹赌杜镀肚度渡妒端短锻段断缎堆兑队对墩吨蹲敦顿囤钝盾遁掇哆多夺垛躲朵跺舵剁惰堕蛾峨鹅俄额讹娥恶厄扼遏鄂饿恩而儿耳尔饵洱二贰发罚筏伐乏阀法珐藩帆番翻樊矾钒繁凡烦反返范贩犯饭泛坊芳方肪房防妨仿访纺放菲非啡飞肥匪诽吠肺废沸费芬酚吩氛分纷坟焚汾粉奋份忿愤粪丰封枫蜂峰锋风疯烽逢冯缝讽奉凤佛否夫敷肤孵扶拂辐幅氟符伏俘服浮涪福袱弗甫抚辅俯釜斧脯腑府腐赴副覆赋复傅付阜父腹负富讣附妇缚咐噶嘎该改概钙盖溉干甘杆柑竿肝赶感秆敢赣冈刚钢缸肛纲岗港杠篙皋高膏羔糕搞镐稿告哥歌搁戈鸽胳疙割革葛格蛤阁隔铬个各给根跟耕更庚羹埂耿梗工攻功恭龚供躬公宫弓巩汞拱贡共钩勾沟苟狗垢构购够辜菇咕箍估沽孤姑鼓古蛊骨谷股故顾固雇刮瓜剐寡挂褂乖拐怪棺关官冠观管馆罐惯灌贯光广逛瑰规圭硅归龟闺轨鬼诡癸桂柜跪贵刽辊滚棍锅郭国果裹过哈骸孩海氦亥害骇酣憨邯韩含涵寒函喊罕翰撼捍旱憾悍焊汗汉夯杭航壕嚎豪毫郝好耗号浩呵喝荷菏核禾和何合盒貉阂河涸赫褐鹤贺嘿黑痕很狠恨哼亨横衡恒轰哄烘虹鸿洪宏弘红喉侯猴吼厚候后呼乎忽瑚壶葫胡蝴狐糊湖弧虎唬护互沪户花哗华猾滑画划化话槐徊怀淮坏欢环桓还缓换患唤痪豢焕涣宦幻荒慌黄磺蝗簧皇凰惶煌晃幌恍谎灰挥辉徽恢蛔回毁悔慧卉惠晦贿秽会烩汇讳诲绘荤昏婚魂浑混豁活伙火获或惑霍货祸击圾基机畸稽积箕肌饥迹激讥鸡姬绩缉吉极棘辑籍集及急疾汲即嫉级挤几脊己蓟技冀季伎祭剂悸济寄寂计记既忌际妓继纪嘉枷夹佳家加荚颊贾甲钾假稼价架驾嫁歼监坚尖笺间煎兼肩艰奸缄茧检柬碱硷拣捡简俭剪减荐槛鉴践贱见键箭件健舰剑饯渐溅涧建僵姜将浆江疆蒋桨奖讲匠酱降蕉椒礁焦胶交郊浇骄娇嚼搅铰矫侥脚狡角饺缴绞剿教酵轿较叫窖揭接皆秸街阶截劫节桔杰捷睫竭洁结解姐戒藉芥界借介疥诫届巾筋斤金今津襟紧锦仅谨进靳晋禁近烬浸尽劲荆兢茎睛晶鲸京惊精粳经井警景颈静境敬镜径痉靖竟竞净炯窘揪究纠玖韭久灸九酒厩救旧臼舅咎就疚鞠拘狙疽居驹菊局咀矩举沮聚拒据巨具距踞锯俱句惧炬剧捐鹃娟倦眷卷绢撅攫抉掘倔爵觉决诀绝均菌钧军君峻俊竣浚郡骏喀咖卡咯开揩楷凯慨刊堪勘坎砍看康慷糠扛抗亢炕考拷烤靠坷苛柯棵磕颗科壳咳可渴克刻客课肯啃垦恳坑吭空恐孔控抠口扣寇枯哭窟苦酷库裤夸垮挎跨胯块筷侩快宽款匡筐狂框矿眶旷况亏盔岿窥葵奎魁傀馈愧溃坤昆捆困括扩廓阔垃拉喇蜡腊辣啦莱来赖蓝婪栏拦篮阑兰澜谰揽览懒缆烂滥琅榔狼廊郎朗浪捞劳牢老佬姥酪烙涝勒乐雷镭蕾磊累儡垒擂肋类泪棱楞冷厘梨犁黎篱狸离漓理李里鲤礼莉荔吏栗丽厉励砾历利傈例俐痢立粒沥隶力璃哩俩联莲连镰廉怜涟帘敛脸链恋炼练粮凉梁粱良两辆量晾亮谅撩聊僚疗燎寥辽潦了撂镣廖料列裂烈劣猎琳林磷霖临邻鳞淋凛赁吝拎玲菱零龄铃伶羚凌灵陵岭领另令溜琉榴硫馏留刘瘤流柳六龙聋咙笼窿隆垄拢陇楼娄搂篓漏陋芦卢颅庐炉掳卤虏鲁麓碌露路赂鹿潞禄录陆戮驴吕铝侣旅履屡缕虑氯律率滤绿峦挛孪滦卵乱掠略抡轮伦仑沦纶论萝螺罗逻锣箩骡裸落洛骆络妈麻玛码蚂马骂嘛吗埋买麦卖迈脉瞒馒蛮满蔓曼慢漫谩芒茫盲氓忙莽猫茅锚毛矛铆卯茂冒帽貌贸么玫枚梅酶霉煤没眉媒镁每美昧寐妹媚门闷们萌蒙檬盟锰猛梦孟眯醚靡糜迷谜弥米秘觅泌蜜密幂棉眠绵冕免勉娩缅面苗描瞄藐秒渺庙妙蔑灭民抿皿敏悯闽明螟鸣铭名命谬摸摹蘑模膜磨摩魔抹末莫墨默沫漠寞陌谋牟某拇牡亩姆母墓暮幕募慕木目睦牧穆拿哪呐钠那娜纳氖乃奶耐奈南男难囊挠脑恼闹淖呢馁内嫩能妮霓倪泥尼拟你匿腻逆溺蔫拈年碾撵捻念娘酿鸟尿捏聂孽啮镊镍涅您柠狞凝宁拧泞牛扭钮纽脓浓农弄奴努怒女暖虐疟挪懦糯诺哦欧鸥殴藕呕偶沤啪趴爬帕怕琶拍排牌徘湃派攀潘盘磐盼畔判叛乓庞旁耪胖抛咆刨炮袍跑泡呸胚培裴赔陪配佩沛喷盆砰抨烹澎彭蓬棚硼篷膨朋鹏捧碰坯砒霹批披劈琵毗啤脾疲皮匹痞僻屁譬篇偏片骗飘漂瓢票撇瞥拼频贫品聘乒坪苹萍平凭瓶评屏坡泼颇婆破魄迫粕剖扑铺仆莆葡菩蒲埔朴圃普浦谱曝瀑期欺栖戚妻七凄漆柒沏其棋奇歧畦崎脐齐旗祈祁骑起岂乞企启契砌器气迄弃汽泣讫掐恰洽牵扦钎铅千迁签仟谦乾黔钱钳前潜遣浅谴堑嵌欠歉枪呛腔羌墙蔷强抢橇锹敲悄桥瞧乔侨巧鞘撬翘峭俏窍切茄且怯窃钦侵亲秦琴勤芹擒禽寝沁青轻氢倾卿清擎晴氰情顷请庆琼穷秋丘邱球求囚酋泅趋区蛆曲躯屈驱渠取娶龋趣去圈颧权醛泉全痊拳犬券劝缺炔瘸却鹊榷确雀裙群然燃冉染瓤壤攘嚷让饶扰绕惹热壬仁人忍韧任认刃妊纫扔仍日戎茸蓉荣融熔溶容绒冗揉柔肉茹蠕儒孺如辱乳汝入褥软阮蕊瑞锐闰润若弱撒洒萨腮鳃塞赛三叁伞散桑嗓丧搔骚扫嫂瑟色涩森僧莎砂杀刹沙纱傻啥煞筛晒珊苫杉山删煽衫闪陕擅赡膳善汕扇缮墒伤商赏晌上尚裳梢捎稍烧芍勺韶少哨邵绍奢赊蛇舌舍赦摄射慑涉社设砷申呻伸身深娠绅神沈审婶甚肾慎渗声生甥牲升绳省盛剩胜圣师失狮施湿诗尸虱十石拾时什食蚀实识史矢使屎驶始式示士世柿事拭誓逝势是嗜噬适仕侍释饰氏市恃室视试收手首守寿授售受瘦兽蔬枢梳殊抒输叔舒淑疏书赎孰熟薯暑曙署蜀黍鼠属术述树束戍竖墅庶数漱恕刷耍摔衰甩帅栓拴霜双爽谁水睡税吮瞬顺舜说硕朔烁斯撕嘶思私司丝死肆寺嗣四伺似饲巳松耸怂颂送宋讼诵搜艘擞嗽苏酥俗素速粟僳塑溯宿诉肃酸蒜算虽隋随绥髓碎岁穗遂隧祟孙损笋蓑梭唆缩琐索锁所塌他它她塔獭挞蹋踏胎苔抬台泰酞太态汰坍摊贪瘫滩坛檀痰潭谭谈坦毯袒碳探叹炭汤塘搪堂棠膛唐糖倘躺淌趟烫掏涛滔绦萄桃逃淘陶讨套特藤腾疼誊梯剔踢锑提题蹄啼体替嚏惕涕剃屉天添填田甜恬舔腆挑条迢眺跳贴铁帖厅听烃汀廷停亭庭挺艇通桐酮瞳同铜彤童桶捅筒统痛偷投头透凸秃突图徒途涂屠土吐兔湍团推颓腿蜕褪退吞屯臀拖托脱鸵陀驮驼椭妥拓唾挖哇蛙洼娃瓦袜歪外豌弯湾玩顽丸烷完碗挽晚皖惋宛婉万腕汪王亡枉网往旺望忘妄威巍微危韦违桅围唯惟为潍维苇萎委伟伪尾纬未蔚味畏胃喂魏位渭谓尉慰卫瘟温蚊文闻纹吻稳紊问嗡翁瓮挝蜗涡窝我斡卧握沃巫呜钨乌污诬屋无芜梧吾吴毋武五捂午舞伍侮坞戊雾晤物勿务悟误昔熙析西硒矽晰嘻吸锡牺稀息希悉膝夕惜熄烯溪汐犀檄袭席习媳喜铣洗系隙戏细瞎虾匣霞辖暇峡侠狭下厦夏吓掀锨先仙鲜纤咸贤衔舷闲涎弦嫌显险现献县腺馅羡宪陷限线相厢镶香箱襄湘乡翔祥详想响享项巷橡像向象萧硝霄削哮嚣销消宵淆晓小孝校肖啸笑效楔些歇蝎鞋协挟携邪斜胁谐写械卸蟹懈泄泻谢屑薪芯锌欣辛新忻心信衅星腥猩惺兴刑型形邢行醒幸杏性姓兄凶胸匈汹雄熊休修羞朽嗅锈秀袖绣墟戌需虚嘘须徐许蓄酗叙旭序畜恤絮婿绪续轩喧宣悬旋玄选癣眩绚靴薛学穴雪血勋熏循旬询寻驯巡殉汛训讯逊迅压押鸦鸭呀丫芽牙蚜崖衙涯雅哑亚讶焉咽阉烟淹盐严研蜒岩延言颜阎炎沿奄掩眼衍演艳堰燕厌砚雁唁彦焰宴谚验殃央鸯秧杨扬佯疡羊洋阳氧仰痒养样漾邀腰妖瑶摇尧遥窑谣姚咬舀药要耀椰噎耶爷野冶也页掖业叶曳腋夜液一壹医揖铱依伊衣颐夷遗移仪胰疑沂宜姨彝椅蚁倚已乙矣以艺抑易邑屹亿役臆逸肄疫亦裔意毅忆义益溢诣议谊译异翼翌绎茵荫因殷音阴姻吟银淫寅饮尹引隐印英樱婴鹰应缨莹萤营荧蝇迎赢盈影颖硬映哟拥佣臃痈庸雍踊蛹咏泳涌永恿勇用幽优悠忧尤由邮铀犹油游酉有友右佑釉诱又幼迂淤于盂榆虞愚舆余俞逾鱼愉渝渔隅予娱雨与屿禹宇语羽玉域芋郁吁遇喻峪御愈欲狱育誉浴寓裕预豫驭鸳渊冤元垣袁原援辕园员圆猿源缘远苑愿怨院曰约越跃钥岳粤月悦阅耘云郧匀陨允运蕴酝晕韵孕匝砸杂栽哉灾宰载再在咱攒暂赞赃脏葬遭糟凿藻枣早澡蚤躁噪造皂灶燥责择则泽贼怎增憎曾赠扎喳渣札轧铡闸眨栅榨咋乍炸诈摘斋宅窄债寨瞻毡詹粘沾盏斩辗崭展蘸栈占战站湛绽樟章彰漳张掌涨杖丈帐账仗胀瘴障招昭找沼赵照罩兆肇召遮折哲蛰辙者锗蔗这浙珍斟真甄砧臻贞针侦枕疹诊震振镇阵蒸挣睁征狰争怔整拯正政帧症郑证芝枝支吱蜘知肢脂汁之织职直植殖执值侄址指止趾只旨纸志挚掷至致置帜峙制智秩稚质炙痔滞治窒中盅忠钟衷终种肿重仲众舟周州洲诌粥轴肘帚咒皱宙昼骤珠株蛛朱猪诸诛逐竹烛煮拄瞩嘱主著柱助蛀贮铸筑住注祝驻抓爪拽专砖转撰赚篆桩庄装妆撞壮状椎锥追赘坠缀谆准捉拙卓桌琢茁酌啄着灼浊兹咨资姿滋淄孜紫仔籽滓子自渍字鬃棕踪宗综总纵邹走奏揍租足卒族祖诅阻组钻纂嘴醉最罪尊遵昨左佐柞做作坐座",
    "亍丌兀丐廿卅丕亘丞鬲孬噩丨禺丿匕乇夭爻卮氐囟胤馗毓睾鼗丶亟鼐乜乩亓芈孛啬嘏仄厍厝厣厥厮靥赝匚叵匦匮匾赜卦卣刂刈刎刭刳刿剀剌剞剡剜蒯剽劂劁劐劓冂罔亻仃仉仂仨仡仫仞伛仳伢佤仵伥伧伉伫佞佧攸佚佝佟佗伲伽佶佴侑侉侃侏佾佻侪佼侬侔俦俨俪俅俚俣俜俑俟俸倩偌俳倬倏倮倭俾倜倌倥倨偾偃偕偈偎偬偻傥傧傩傺僖儆僭僬僦僮儇儋仝氽佘佥俎龠汆籴兮巽黉馘冁夔勹匍訇匐凫夙兕亠兖亳衮袤亵脔裒禀嬴蠃羸冫冱冽冼凇冖冢冥讠讦讧讪讴讵讷诂诃诋诏诎诒诓诔诖诘诙诜诟诠诤诨诩诮诰诳诶诹诼诿谀谂谄谇谌谏谑谒谔谕谖谙谛谘谝谟谠谡谥谧谪谫谮谯谲谳谵谶卩卺阝阢阡阱阪阽阼陂陉陔陟陧陬陲陴隈隍隗隰邗邛邝邙邬邡邴邳邶邺邸邰郏郅邾郐郄郇郓郦郢郜郗郛郫郯郾鄄鄢鄞鄣鄱鄯鄹酃酆刍奂劢劬劭劾哿勐勖勰叟燮矍廴凵凼鬯厶弁畚巯坌垩垡塾墼壅壑圩圬圪圳圹圮圯坜圻坂坩垅坫垆坼坻坨坭坶坳垭垤垌垲埏垧垴垓垠埕埘埚埙埒垸埴埯埸埤埝堋堍埽埭堀堞堙塄堠塥塬墁墉墚墀馨鼙懿艹艽艿芏芊芨芄芎芑芗芙芫芸芾芰苈苊苣芘芷芮苋苌苁芩芴芡芪芟苄苎芤苡茉苷苤茏茇苜苴苒苘茌苻苓茑茚茆茔茕苠苕茜荑荛荜茈莒茼茴茱莛荞茯荏荇荃荟荀茗荠茭茺茳荦荥荨茛荩荬荪荭荮莰荸莳莴莠莪莓莜莅荼莶莩荽莸荻莘莞莨莺莼菁萁菥菘堇萘萋菝菽菖萜萸萑萆菔菟萏萃菸菹菪菅菀萦菰菡葜葑葚葙葳蒇蒈葺蒉葸萼葆葩葶蒌蒎萱葭蓁蓍蓐蓦蒽蓓蓊蒿蒺蓠蒡蒹蒴蒗蓥蓣蔌甍蔸蓰蔹蔟蔺蕖蔻蓿蓼蕙蕈蕨蕤蕞蕺瞢蕃蕲蕻薤薨薇薏蕹薮薜薅薹薷薰藓藁藜藿蘧蘅蘩蘖蘼廾弈夼奁耷奕奚奘匏尢尥尬尴扌扪抟抻拊拚拗拮挢拶挹捋捃掭揶捱捺掎掴捭掬掊捩掮掼揲揸揠揿揄揞揎摒揆掾摅摁搋搛搠搌搦搡摞撄摭撖摺撷撸撙撺擀擐擗擤擢攉攥攮弋忒甙弑卟叱叽叩叨叻吒吖吆呋呒呓呔呖呃吡呗呙吣吲咂咔呷呱呤咚咛咄呶呦咝哐咭哂咴哒咧咦哓哔呲咣哕咻咿哌哙哚哜咩咪咤哝哏哞唛哧唠哽唔哳唢唣唏唑唧唪啧喏喵啉啭啁啕唿啐唼唷啖啵啶啷唳唰啜喋嗒喃喱喹喈喁喟啾嗖喑啻嗟喽喾喔喙嗪嗷嗉嘟嗑嗫嗬嗔嗦嗝嗄嗯嗥嗲嗳嗌嗍嗨嗵嗤辔嘞嘈嘌嘁嘤嘣嗾嘀嘧嘭噘嘹噗嘬噍噢噙噜噌噔嚆噤噱噫噻噼嚅嚓嚯囔囗囝囡囵囫囹囿圄圊圉圜帏帙帔帑帱帻帼帷幄幔幛幞幡岌屺岍岐岖岈岘岙岑岚岜岵岢岽岬岫岱岣峁岷峄峒峤峋峥崂崃崧崦崮崤崞崆崛嵘崾崴崽嵬嵛嵯嵝嵫嵋嵊嵩嵴嶂嶙嶝豳嶷巅彳彷徂徇徉後徕徙徜徨徭徵徼衢彡犭犰犴犷犸狃狁狎狍狒狨狯狩狲狴狷猁狳猃狺狻猗猓猡猊猞猝猕猢猹猥猬猸猱獐獍獗獠獬獯獾舛夥飧夤夂饣饧饨饩饪饫饬饴饷饽馀馄馇馊馍馐馑馓馔馕庀庑庋庖庥庠庹庵庾庳赓廒廑廛廨廪膺忄忉忖忏怃忮怄忡忤忾怅怆忪忭忸怙怵怦怛怏怍怩怫怊怿怡恸恹恻恺恂恪恽悖悚悭悝悃悒悌悛惬悻悱惝惘惆惚悴愠愦愕愣惴愀愎愫慊慵憬憔憧憷懔懵忝隳闩闫闱闳闵闶闼闾阃阄阆阈阊阋阌阍阏阒阕阖阗阙阚丬爿戕氵汔汜汊沣沅沐沔沌汨汩汴汶沆沩泐泔沭泷泸泱泗沲泠泖泺泫泮沱泓泯泾洹洧洌浃浈洇洄洙洎洫浍洮洵洚浏浒浔洳涑浯涞涠浞涓涔浜浠浼浣渚淇淅淞渎涿淠渑淦淝淙渖涫渌涮渫湮湎湫溲湟溆湓湔渲渥湄滟溱溘滠漭滢溥溧溽溻溷滗溴滏溏滂溟潢潆潇漤漕滹漯漶潋潴漪漉漩澉澍澌潸潲潼潺濑濉澧澹澶濂濡濮濞濠濯瀚瀣瀛瀹瀵灏灞宀宄宕宓宥宸甯骞搴寤寮褰寰蹇謇辶迓迕迥迮迤迩迦迳迨逅逄逋逦逑逍逖逡逵逶逭逯遄遑遒遐遨遘遢遛暹遴遽邂邈邃邋彐彗彖彘尻咫屐屙孱屣屦羼弪弩弭艴弼鬻屮妁妃妍妩妪妣妗姊妫妞妤姒妲妯姗妾娅娆姝娈姣姘姹娌娉娲娴娑娣娓婀婧婊婕娼婢婵胬媪媛婷婺媾嫫媲嫒嫔媸嫠嫣嫱嫖嫦嫘嫜嬉嬗嬖嬲嬷孀尕尜孚孥孳孑孓孢驵驷驸驺驿驽骀骁骅骈骊骐骒骓骖骘骛骜骝骟骠骢骣骥骧纟纡纣纥纨纩纭纰纾绀绁绂绉绋绌绐绔绗绛绠绡绨绫绮绯绱绲缍绶绺绻绾缁缂缃缇缈缋缌缏缑缒缗缙缜缛缟缡缢缣缤缥缦缧缪缫缬缭缯缰缱缲缳缵幺畿巛甾邕玎玑玮玢玟珏珂珑玷玳珀珉珈珥珙顼琊珩珧珞玺珲琏琪瑛琦琥琨琰琮琬琛琚瑁瑜瑗瑕瑙瑷瑭瑾璜璎璀璁璇璋璞璨璩璐璧瓒璺韪韫韬杌杓杞杈杩枥枇杪杳枘枧杵枨枞枭枋杷杼柰栉柘栊柩枰栌柙枵柚枳柝栀柃枸柢栎柁柽栲栳桠桡桎桢桄桤梃栝桕桦桁桧桀栾桊桉栩梵梏桴桷梓桫棂楮棼椟椠棹椤棰椋椁楗棣椐楱椹楠楂楝榄楫榀榘楸椴槌榇榈槎榉楦楣楹榛榧榻榫榭槔榱槁槊槟榕槠榍槿樯槭樗樘橥槲橄樾檠橐橛樵檎橹樽樨橘橼檑檐檩檗檫猷獒殁殂殇殄殒殓殍殚殛殡殪轫轭轱轲轳轵轶轸轷轹轺轼轾辁辂辄辇辋辍辎辏辘辚軎戋戗戛戟戢戡戥戤戬臧瓯瓴瓿甏甑甓攴旮旯旰昊昙杲昃昕昀炅曷昝昴昱昶昵耆晟晔晁晏晖晡晗晷暄暌暧暝暾曛曜曦曩贲贳贶贻贽赀赅赆赈赉赇赍赕赙觇觊觋觌觎觏觐觑牮犟牝牦牯牾牿犄犋犍犏犒挈挲掰搿擘耄毪毳毽毵毹氅氇氆氍氕氘氙氚氡氩氤氪氲攵敕敫牍牒牖爰虢刖肟肜肓肼朊肽肱肫肭肴肷胧胨胩胪胛胂胄胙胍胗朐胝胫胱胴胭脍脎胲胼朕脒豚脶脞脬脘脲腈腌腓腴腙腚腱腠腩腼腽腭腧塍媵膈膂膑滕膣膪臌朦臊膻臁膦欤欷欹歃歆歙飑飒飓飕飙飚殳彀毂觳斐齑斓於旆旄旃旌旎旒旖炀炜炖炝炻烀炷炫炱烨烊焐焓焖焯焱煳煜煨煅煲煊煸煺熘熳熵熨熠燠燔燧燹爝爨灬焘煦熹戾戽扃扈扉礻祀祆祉祛祜祓祚祢祗祠祯祧祺禅禊禚禧禳忑忐怼恝恚恧恁恙恣悫愆愍慝憩憝懋懑戆肀聿沓泶淼矶矸砀砉砗砘砑斫砭砜砝砹砺砻砟砼砥砬砣砩硎硭硖硗砦硐硇硌硪碛碓碚碇碜碡碣碲碹碥磔磙磉磬磲礅磴礓礤礞礴龛黹黻黼盱眄眍盹眇眈眚眢眙眭眦眵眸睐睑睇睃睚睨睢睥睿瞍睽瞀瞌瞑瞟瞠瞰瞵瞽町畀畎畋畈畛畲畹疃罘罡罟詈罨罴罱罹羁罾盍盥蠲钅钆钇钋钊钌钍钏钐钔钗钕钚钛钜钣钤钫钪钭钬钯钰钲钴钶钷钸钹钺钼钽钿铄铈铉铊铋铌铍铎铐铑铒铕铖铗铙铘铛铞铟铠铢铤铥铧铨铪铩铫铮铯铳铴铵铷铹铼铽铿锃锂锆锇锉锊锍锎锏锒锓锔锕锖锘锛锝锞锟锢锪锫锩锬锱锲锴锶锷锸锼锾锿镂锵镄镅镆镉镌镎镏镒镓镔镖镗镘镙镛镞镟镝镡镢镤镥镦镧镨镩镪镫镬镯镱镲镳锺矧矬雉秕秭秣秫稆嵇稃稂稞稔稹稷穑黏馥穰皈皎皓皙皤瓞瓠甬鸠鸢鸨鸩鸪鸫鸬鸲鸱鸶鸸鸷鸹鸺鸾鹁鹂鹄鹆鹇鹈鹉鹋鹌鹎鹑鹕鹗鹚鹛鹜鹞鹣鹦鹧鹨鹩鹪鹫鹬鹱鹭鹳疒疔疖疠疝疬疣疳疴疸痄疱疰痃痂痖痍痣痨痦痤痫痧瘃痱痼痿瘐瘀瘅瘌瘗瘊瘥瘘瘕瘙瘛瘼瘢瘠癀瘭瘰瘿瘵癃瘾瘳癍癞癔癜癖癫癯翊竦穸穹窀窆窈窕窦窠窬窨窭窳衤衩衲衽衿袂袢裆袷袼裉裢裎裣裥裱褚裼裨裾裰褡褙褓褛褊褴褫褶襁襦襻疋胥皲皴矜耒耔耖耜耠耢耥耦耧耩耨耱耋耵聃聆聍聒聩聱覃顸颀颃颉颌颍颏颔颚颛颞颟颡颢颥颦虍虔虬虮虿虺虼虻蚨蚍蚋蚬蚝蚧蚣蚪蚓蚩蚶蛄蚵蛎蚰蚺蚱蚯蛉蛏蚴蛩蛱蛲蛭蛳蛐蜓蛞蛴蛟蛘蛑蜃蜇蛸蜈蜊蜍蜉蜣蜻蜞蜥蜮蜚蜾蝈蜴蜱蜩蜷蜿螂蜢蝽蝾蝻蝠蝰蝌蝮螋蝓蝣蝼蝤蝙蝥螓螯螨蟒蟆螈螅螭螗螃螫蟥螬螵螳蟋蟓螽蟑蟀蟊蟛蟪蟠蟮蠖蠓蟾蠊蠛蠡蠹蠼缶罂罄罅舐竺竽笈笃笄笕笊笫笏筇笸笪笙笮笱笠笥笤笳笾笞筘筚筅筵筌筝筠筮筻筢筲筱箐箦箧箸箬箝箨箅箪箜箢箫箴篑篁篌篝篚篥篦篪簌篾篼簏簖簋簟簪簦簸籁籀臾舁舂舄臬衄舡舢舣舭舯舨舫舸舻舳舴舾艄艉艋艏艚艟艨衾袅袈裘裟襞羝羟羧羯羰羲籼敉粑粝粜粞粢粲粼粽糁糇糌糍糈糅糗糨艮暨羿翎翕翥翡翦翩翮翳糸絷綦綮繇纛麸麴赳趄趔趑趱赧赭豇豉酊酐酎酏酤酢酡酰酩酯酽酾酲酴酹醌醅醐醍醑醢醣醪醭醮醯醵醴醺豕鹾趸跫踅蹙蹩趵趿趼趺跄跖跗跚跞跎跏跛跆跬跷跸跣跹跻跤踉跽踔踝踟踬踮踣踯踺蹀踹踵踽踱蹉蹁蹂蹑蹒蹊蹰蹶蹼蹯蹴躅躏躔躐躜躞豸貂貊貅貘貔斛觖觞觚觜觥觫觯訾謦靓雩雳雯霆霁霈霏霎霪霭霰霾龀龃龅龆龇龈龉龊龌黾鼋鼍隹隼隽雎雒瞿雠銎銮鋈錾鍪鏊鎏鐾鑫鱿鲂鲅鲆鲇鲈稣鲋鲎鲐鲑鲒鲔鲕鲚鲛鲞鲟鲠鲡鲢鲣鲥鲦鲧鲨鲩鲫鲭鲮鲰鲱鲲鲳鲴鲵鲶鲷鲺鲻鲼鲽鳄鳅鳆鳇鳊鳋鳌鳍鳎鳏鳐鳓鳔鳕鳗鳘鳙鳜鳝鳟鳢靼鞅鞑鞒鞔鞯鞫鞣鞲鞴骱骰骷鹘骶骺骼髁髀髅髂髋髌髑魅魃魇魉魈魍魑飨餍餮饕饔髟髡髦髯髫髻髭髹鬈鬏鬓鬟鬣麽麾縻麂麇麈麋麒鏖麝麟黛黜黝黠黟黢黩黧黥黪黯鼢鼬鼯鼹鼷鼽鼾齄"
]

现汉通字表 = [
    "一乙二十丁厂七卜八人入乂儿九匕几刁了乃刀力又乜三干亍于亏士土工才下寸丈大兀与万弋上小口山巾千乞川亿彳个么久勺丸夕凡及广亡门丫义之尸已巳弓己卫孑子孓也女飞刃习叉马乡幺丰王井开亓夫天元无韦云专丐扎廿艺木五支厅卅不仄太犬区历友歹尤匹厄车巨牙屯戈比互切瓦止少曰日中贝内水冈见手午牛毛气壬升夭长仁仃什片仆仉化仇币仂仍仅斤爪反兮刈介父爻从仑今凶分乏公仓月氏勿风欠丹匀乌勾殳凤卞六文亢方闩火为斗忆计订户讣认讥冗心尹尺夬引丑爿巴孔队办以允邓予劝双书毋幻玉刊末未示击邗戋打巧正扑卉扒邛功扔去甘世艾艽古节艿本术札可叵匝丙左厉丕石右布夯龙戊平灭轧东匜劢卡北占凸卢业旧帅归目旦且叮叶甲申号电田由卟叭只央史叱叽兄叼叩叫叻叨另叹冉皿凹囚四生失矢氕乍禾仨仕丘付仗代仙仟仡仫伋们仪白仔他仞斥卮瓜乎丛令用甩印氐乐尔句匆犰册卯犯外处冬鸟务刍包饥主市庀邝立冯邙玄闪兰半汀汁汇头汈汉忉宁穴宄它讦讧讨写让礼讪讫训必议讯记永司尻尼民弗弘阢出阡辽奶奴尕加召皮边发孕圣对弁台矛纠驭母幼丝匡耒邦玎玑式迂刑邢戎动圩圬圭扛寺吉扣扦圪考托圳老圾巩执扩圹扪扫圯圮地扬场耳芋芏共芊芍芨芄芒亚芝芎芑芗朽朴机权过亘臣吏再协西压厌厍戌在百有存而页匠夸夺夼灰达戍尥列死成夹夷轨邪尧划迈毕至此乩贞师尘尖劣光当吁早吐吓旯曳虫曲团同吕吊吃因吸吗吆屿屹岌帆岁回岂屺则刚网肉凼囝囡钆钇年朱缶氘氖牝先丢廷舌竹迁乔迄伟传乒乓休伍伎伏伛优臼伢伐仳延佤仲仵件任伤伥价伦份伧华仰伉仿伙伪伫自伊血向囟似后行甪舟全会杀合兆企汆氽众爷伞创刖肌肋朵杂夙危旬旭旮旨负犴刎犷匈犸舛各名多凫争邬色饧冱壮冲妆冰庄庆亦刘齐交次衣产决亥邡充妄闭问闯羊并关米灯州汗污江汕汔汲汐汛汜池汝汤汊忖忏忙兴宇守宅字安讲讳讴军讵讶祁讷许讹论讼农讽设访诀聿寻那艮厾迅尽导异弛阱阮孙阵阳收阪阶阴防丞奸如妁妇妃好她妈戏羽观牟欢买纡红纣驮纤纥驯纨约级纩纪驰纫巡寿玕弄玙麦玖玚玛形进戒吞远违韧运扶抚坛抟技坏抔抠坜扰扼拒找批扯址走抄汞坝贡攻赤圻折抓扳坂抡扮抢扺孝坎坍均坞抑抛投抃坟坑抗坊抖护壳志扭块抉声把报拟抒却劫毐芙芫芜苇邯芸芾芰苈苊苣芽芷芮苋芼苌花芹芥苁芩芬苍芪芴芡芟苄芳严苎芦芯劳克芭苏苡杆杜杠材村杖杌杏杉巫杓极杧杞李杨杈求忑孛甫匣更束吾豆两邴酉丽医辰励邳否还矶奁豕尬歼来忒连欤轩轪轫迓邶忐芈步卤卣邺坚肖旰旱盯呈时吴呋助县里呓呆吱吠呔呕园呖呃旷围呀吨旸吡町足虬邮男困吵串呙呐呗员听吟吩呛吻吹呜吭吣吲吼邑吧囤别吮岍帏岐岖岈岗岘帐岑岚兕财囵囫钉针钊钋钌迕氙氚牡告我乱利秃秀私岙每佞兵邱估体何佐伾佑攸但伸佃佚作伯伶佣低你佝佟住位伴佗身皂伺佛伽囱近彻役彷返佘余希佥坐谷孚妥豸含邻坌岔肝肟肛肚肘肠邸龟甸奂免劬狂犹狈狄角删狃狁鸠条彤卵灸岛邹刨饨迎饩饪饫饬饭饮系言冻状亩况亨庑床庋库庇疔疖疗吝应冷这庐序辛肓弃冶忘闰闱闲闳间闵闶闷羌判兑灶灿灼炀弟沣汪沅沄沐沛沔汰沤沥沌沘沏沚沙汩汨汭汽沃沂沦汹汾泛沧沨沟没汴汶沆沩沪沈沉沁泐怃忮怀怄忧忡忤忾怅忻忪怆忭忱快忸完宋宏牢究穷灾良证诂诃启评补初社祀祃诅识诈诉罕诊诋诌词诎诏诐译诒君灵即层屁屃尿尾迟局改张忌际陆阿孜陇陈阽阻阼附坠陀陂陉妍妩妓妪妣妙妊妖妗姊妨妫妒妞姒妤努邵劭忍刭劲甬邰矣鸡纬纭驱纯纰纱纲纳纴纵驳纶纷纸纹纺纻驴纽纾奉玩玮环玡武青责现玫玠玢玥表玦甙盂忝规匦抹卦邽坩坷坯拓垅拢拔抨坪拣拤拈坫垆坦担坤押抻抽拐拃拖拊者拍顶坼拆拎拥抵坻拘势抱拄垃拉拦幸拌拧坨坭抿拂拙招坡披拨择拚抬拇坳拗耵其耶取茉苷苦苯昔苛苤若茂茏苹苫苴苜苗英苒苘茌苻苓茚苟茆茑苑苞范茓茔茕直苠茀茁茄苕茎苔茅枉林枝杯枢枥柜枇杪杳枘枧杵枚枨析板枞松枪枫构杭枋杰述枕杻杷杼丧或画卧事刺枣雨卖矸郁矻矾矽矿砀码厕奈刳奔奇奄奋态瓯欧殴垄殁郏妻轰顷转轭斩轮软到郅鸢非叔歧肯齿些卓虎虏肾贤尚盱旺具昊昙果味杲昃昆国哎咕昌呵咂畅呸昕明易咙昀昂旻昉炅咔畀虮迪典固忠咀呷呻黾咒咋咐呱呼呤咚鸣咆咛咏呢咄呶咖呦咝岵岢岸岩帖罗岿岬岫帜帙帕岭岣峁刿峂迥岷剀凯帔峄沓败账贩贬购贮囹图罔钍钎钏钐钓钒钔钕钗邾制知迭氛迮垂牦牧物乖刮秆和季委竺秉迤佳侍佶岳佬佴供使侑佰侉例侠臾侥版侄岱侦侣侗侃侧侏凭侨侩佻佾佩货侈侪佼依佯侬帛卑的迫阜侔质欣郈征徂往爬彼径所舍金刽郐刹命肴郄斧怂爸采籴觅受乳贪念贫忿瓮戗肼肤朊肺肢肽肱肫肿肭胀朋肷股肮肪肥服胁周剁昏迩郇鱼兔狉狙狎狐忽狝狗狍狞狒咎备炙枭饯饰饱饲饳饴冽变京享冼庞店夜庙府底庖疟疠疝疙疚疡剂卒郊兖庚废净妾盲放刻於劾育氓闸闹郑券卷单炜炬炖炒炝炊炕炎炉炔沫浅法泔泄沽沭河泷沾泸沮泪油泱泅泗泊泠泜泺泃沿泖泡注泣泫泮泞沱泻泌泳泥泯沸泓沼波泼泽泾治怔怯怙怵怖怦怛怏性怍怕怜怩怫怊怿怪怡学宝宗定宕宠宜审宙官空帘穸穹宛实宓诓诔试郎诖诗诘戾肩房诙戽诚郓衬衫衩祆祎祉视祈诛诜话诞诟诠诡询诣诤该详诧诨诩建肃隶录帚屉居届刷鸤屈弧弥弦承孟陋戕陌孤孢陕亟降函陔限卺妹姑姐妲妯姓姗妮始帑弩孥驽姆虱迦迢驾叁参迨艰线绀绁绂练驵组绅细驶织驷驸驹终绉驺驻绊驼绋绌绍驿绎经骀贯甾砉耔契贰奏春帮珏珐珂珑玷玳珀顸珍玲珊珉珈玻毒型韨拭挂封持拮拷拱垭挝垣项垮挎垯挞城挟挠垤政赴赵赳贲垱挡拽垌哉垲挺括挢埏郝垍垧垢拴拾挑垛指垫挣挤垓垟拼垞挖按挥挦挪垠拯拶某甚荆茸革茜茬荐荙巷荚荑贳荛荜茈带草茧茼莒茵茴茱莛荞茯荏荇荃荟茶荀茗荠茭茨荒垩茳茫荡荣荤荥荦荧荨茛故荩胡荪荫茹荔南荬荭药柰标栈柑枯栉柯柄柘栊柩枰栋栌相查柙枵柚枳柞柏柝栀柃柢栎枸栅柳柱柿栏柈柠柁枷柽树勃剌郚剅要酊郦柬咸威歪甭研砖厘砗厚砑砘砒砌砂泵砚斫砭砜砍面耐耍奎耷牵鸥虺残殂殃殇殄殆轱轲轳轴轵轶轷轸轹轺轻鸦虿皆毖韭背战觇点虐临览竖尜省削尝哐昧眄眍盹是郢眇眊盼眨昽眈哇咭哄哑显冒映禺哂星昨咴曷昴咧昱昵咦哓昭哔畎畏毗趴呲胄胃贵畋畈界虹虾虼虻蚁思蚂盅咣虽品咽骂哕剐郧勋咻哗囿咱咿响哌哙哈哚咯哆咬咳咩咪咤哝哪哏哞哟峙炭峡峣罘帧罚峒峤峋峥峧帡贱贴贶贻骨幽钘钙钚钛钝钞钟钡钠钢钣钤钥钦钧钨钩钪钫钬钭钮钯卸缸拜看矩矧毡氡氟氢牯怎郜牲选适秕秒香种秭秋科重复竽竿笈笃俦段俨俅便俩俪叟垡贷牮顺修俏俣俚保俜促俄俐侮俭俗俘信皇泉皈鬼侵禹侯追俑俟俊盾逅待徊徇徉衍律很须舢舣叙俞弇郗剑逃俎郤爰郛食瓴盆胚胧胨胩胪胆胛胂胜胙胍胗胝朐胞胖脉胫胎鸨匍勉狨狭狮独狯狰狡飐飑狩狱狠狲訇訄逄昝贸怨急饵饶蚀饷饸饹饺饻胤饼峦弯孪娈将奖哀亭亮庤度弈奕迹庭庥疬疣疥疭疮疯疫疢疤庠咨姿亲竑音彦飒帝施闺闻闼闽闾闿阀阁阂差养美羑姜迸叛送类籼迷籽娄前酋首逆兹总炳炻炼炟炽炯炸烀烁炮炷炫烂烃剃洼洁洱洪洹洒洧洌浃柒浇泚浈浉浊洞洇洄测洙洗活洑涎洎洫派浍洽洮染洵洚洺洛浏济洨浐洋洴洣洲浑浒浓津浔浕洳恸恃恒恹恢恍恫恺恻恬恤恰恂恪恼恽恨举觉宣宦宥宬室宫宪突穿窀窃客诫冠诬语扁扃袆衲衽袄衿袂祛祜祓祖神祝祚诮祗祢祠误诰诱诲诳鸩说昶诵郡垦退既屋昼咫屏屎弭费陡逊牁眉胥孩陛陟陧陨除险院娃姞姥娅姨娆姻姝娇姚姽姣姘姹娜怒架贺盈怼羿勇炱怠癸蚤柔矜垒绑绒结绔骁绕骄骅绗绘给绚彖绛络骆绝绞骇统骈耕耘耖耗耙艳挈恝泰秦珥珙顼珰珠珽珩珧珣珞琤班珲敖素匿蚕顽盏匪恚捞栽捕埔埂捂振载赶起盐捎捍埕捏埘埋捉捆捐埚埙损袁挹捌都哲逝耆耄捡挫捋埒换挽贽挚热恐捣垸壶捃捅盍埃挨耻耿耽聂莰茝荸莆恭莽莱莲莳莫莴莪莉莠莓荷莜莅荼莶莩荽获莸荻莘晋恶莎莞莹莨莺真莙鸪莼框梆桂桔栲栳郴桓栖桡桎桢桄档桐桤株梃栝桥桕桦桁栓桧桃桅栒格桩校核样栟桉根栩逑索逋彧哥速鬲豇逗栗贾酐酎酌配酏逦翅辱唇厝孬夏砝砹砸砺砰砧砷砟砼砥砾砣础破硁恧原套剞逐砻烈殊殉顾轼轾轿辀辁辂较鸫顿趸毙致剕龀柴桌鸬虔虑监紧逍党眬唛逞晒晟眩眠晓眙唝哧哳哮唠鸭晃哺哽唔晔晌晁剔晏晖晕鸮趵趿畛蚌蚨蚜蚍蚋蚬畔蚝蚧蚣蚊蚪蚓哨唢哩圃哭圄哦唣唏恩盎唑鸯唤唁哼唧啊唉唆帱崂崃罡罢罟峭峨峪峰圆觊峻贼贿赂赃赅赆钰钱钲钳钴钵钷钹钺钻钼钽钾钿铀铁铂铃铄铅铆铈铉铊铋铌铍铎眚缺氩氤氦氧氨毪特牺造乘敌舐秣秫秤租秧积盉秩称秘透笄笕笔笑笊笫笏笋笆俸倩债俵倻借偌值倚俺倾倒俳俶倬倏倘俱倡候赁恁倭倪俾倜隼隽倞俯倍倦倓倌倥臬健臭射皋躬息郫倨倔衄颀徒徕徐殷舰舨舱般航舫瓞途拿釜耸爹舀爱豺豹奚鬯衾鸰颁颂翁胯胰胱胴胭脍脎脆脂胸胳脏脐胶脑胲胼朕脒胺脓鸱玺鱽鸲逛狴狸狷猁狳猃狺逖狼卿狻逢桀鸵留袅眢鸳皱饽饿馀馁凌凇凄栾挛恋桨浆衰勍衷高亳郭席准座脊症疳疴病疽疸疾痄斋疹痈疼疱疰痃痂疲痉效离衮紊唐凋颃瓷资恣凉站剖竞部旁旆旄旅旃畜阃阄阅阆羞羔恙瓶桊拳敉粉料粑益兼朔郸烤烘烜烦烧烛烟烨烩烙烊剡郯烬递涛浙涝浡浦涑浯酒涞涟涉娑消涅涠浞涓涢涡浥涔浩海浜涂浠浴浮涣浼涤流润涧涕浣浪浸涨烫涩涌涘浚悖悚悟悭悄悍悝悃悒悔悯悦悌悢悛害宽宸家宵宴宾窍窅窄容窈剜宰案请朗诸诹诺读扅诼冢扇诽袜袪袒袖袗袍袢被袯祯祧祥课冥诿谀谁谂调冤谄谅谆谇谈谊剥恳展剧屑屐屙弱陵陬勐奘疍牂蚩祟陲陴陶陷陪姬娠娱娌娉娟娲恕娥娩娴娣娘娓婀砮哿畚通能难逡预桑剟绠骊绡骋绢绣验绤绥绦骍继绨骎骏邕烝鸶彗耜焘舂琎球琏琐理琇麸琉琅捧掭堵揶措描埴域捺掎埼掩埯捷捯排焉掉掳掴埸堌捶赦赧推堆捭埠晢掀逵授捻埝堋教堍掏掐掬鸷掠掂掖培掊接堉掷掸控捩掮探悫埭埽据掘掺掇掼职聃基聆勘聊聍娶菁菝著菱萁菥菘堇勒黄萘萋勚菲菽菖萌萜萝菌萎萸萑菂菜棻菔菟萄萏菊萃菩菼菏萍菹菠菪菅菀萤营萦乾萧菰菡萨菇械梽彬梵梦婪梗梧梾梢梏梅觋检桴桷梓梳棁梯桫棂桶梭救啬郾匮曹敕副豉票鄄酝酞酗酚厢厣戚戛硎硅硭硒硕硖硗硐硚硇硌鸸瓠匏奢盔爽厩聋龚袭殒殓殍盛赉匾雩雪辄辅辆堑龁颅虚彪雀敝堂常眶眭唪眦啧匙晡晤晨眺眵睁眯眼眸悬野圊啪啦喏喵啉勖曼晦晞晗晚冕啄啭啡畦趼趺距趾啃跃啮跄略蚶蛄蛎蛆蚰蚺蛊圉蚱蚯蛉蛀蛇蛏蚴唬累鄂唱患啰唾唯啤啥啁啕唿啐唼唷啴啖啵啶啷唳啸啜帻崖崎崦崭逻帼崮崔帷崟崤崩崞崇崆崛赇赈婴赊圈铐铑铒铕铗铘铙铚铛铜铝铞铟铠铡铢铣铤铥铧铨铩铪铫铭铬铮铯铰铱铲铳铴铵银铷矫氪牾甜鸹秸梨犁稆秽移秾逶笺筇笨笸笼笪笛笙笮符笱笠笥第笳笤笾笞敏偾做鸺偃偕袋悠偿偶偈偎偲傀偷您偬售停偻偏躯皑兜皎假衅鸻徘徙徜得衔舸舻舳盘舴舶船鸼舷舵斜龛盒鸽瓻敛悉欲彩领翎脚脖脯豚脶脸脞脬脱脘脲朘匐鱾象够逸猜猪猎猫猗凰猖猡猊猞猄猝斛觖猕猛馗祭馃馄馅馆凑减鸾毫孰烹庶庹麻庵庼庾庳痔痍疵痊痒痕廊康庸鹿盗章竟翊商旌族旎旋望袤率阇阈阉阊阋阌阍阎阏阐着羚羝羟盖眷粝粘粗粕粒断剪兽焐焊烯焓焕烽焖烷烺焌清渍添渚鸿淇淋淅淞渎涯淹涿渠渐淑淖挲淌淏混淠涸渑淮淦淆渊淫淝渔淘淳液淬涪淤淡淙淀涫深渌涮涵婆梁渗淄情惬悻惜惭悱悼惝惧惕惘悸惟惆惚惊惇惦悴惮惋惨惯寇寅寄寂逭宿窒窑窕密谋谌谍谎谏扈皲谐谑裆袱袼裈裉祷祸祲谒谓谔谕谖谗谙谚谛谜谝逮逯敢尉屠艴弹隋堕郿随蛋隅隈粜隍隗隆隐婧婊婞婳婕娼婢婚婵婶婉胬袈颇颈翌恿欸绩绪绫骐续骑绮绯绰骒绲绳骓维绵绶绷绸绹绺绻综绽绾绿骖缀缁巢耠琫琵琴琶琪瑛琳琦琢琥琨靓琼斑琰琮琯琬琛琚辇替鼋揳揍款堪堞搽塔搭塃揸堰揠堙揩越趄趁趋超揽提堤揖博揾颉揭喜彭揣塄揿插揪搜煮堠耋揄援搀蛰蛩絷塆裁揞搁搓搂搅揎壹握摒揆搔揉掾葜聒斯期欺联葑葚葫靰靸散葳惹蒇葬蒈募葺葛蒉葸萼蓇萩董葆葩葡敬葱蒋葶蒂蒌葓蒎落萱葖韩戟朝葭辜葵棒楮棱棋椰植森棼焚椟椅椒棹棵棍椤棰椎棉椑鹀赍棚椋椁棬棕棺榔楗棣椐椭鹁惠惑逼覃粟棘酣酤酢酥酡酦鹂觌厨厦硬硝硪硷确硫雁厥殖裂雄殚殛颊雳雯辊辋椠暂辌辍辎雅翘辈斐悲紫黹凿辉敞棠牚赏掌晴睐暑最晰量睑睇鼎睃喷戢喋嗒喃喳晶喇遇喊喱喹遏晷晾景喈畴践跖跋跌跗跞跚跑跎跏跛跆遗蛙蛱蛲蛭蛳蛐蛔蛛蜓蛞蜒蛤蛴蛟蛘蛑畯喁喝鹃喂喟斝喘啾嗖喤喉喻喑啼嗟喽嗞喧喀喔喙嵌嵘嵖幅崴遄詈帽嵎崽嵚嵬嵛翙嵯嵝嵫幄嵋赋赌赎赐赑赔黑铸铹铺铻铼铽链铿销锁锃锄锂锅锆锇锈锉锊锋锌锎锏锐锑锒锓锔锕甥掣掰短智矬氰毳毯氮毽氯犊犄犋鹄犍鹅颋剩嵇稍程稀黍稃税稂筐等筘筑策筚筛筜筒筅筏筵筌答筋筝傣傲傅傈舄牍牌傥堡集焦傍傧储遑皓皖粤奥傩遁街惩御徨循舾艇舒畲弑逾颌翕釉番释鹆禽舜貂腈腊腌腓腆腙腴脾腋腑腚腔腕腱腒鱿鲀鲁鲂鲃颍猢猹猩猥猬猾猴飓觞觚猸猱惫飧然馇馈馉馊馋亵装蛮脔就敦裒廋斌痣痨痦痘痞痢痤痪痫痧痛鄌赓竦童瓿竣啻颏鹇阑阒阔阕善翔羡普粪粞尊奠遒道遂孳曾焯焜焰焙焱鹈湛港渫滞湖湘渣渤湮湎湝湨湜渺湿温渴渭溃湍溅滑湃湫溲湟溆渝湲湾渡游溠溇湔滋湉渲溉渥湄滁愤慌惰愠惺愦愕惴愣愀愎惶愧愉愔慨喾割寒富寓窜窝窖窗窘寐谟扉遍棨雇扊裢裎裣裕裤裥裙祾祺祼谠禅禄幂谡谢谣谤谥谦谧塈遐犀属屡孱弼强粥巽疏隔骘隙隘媒媪絮嫂媛婷媚婿巯毵翚登皴婺骛缂缃缄缅彘缆缇缈缉缌缎缏缑缒缓缔缕骗编缗骙骚缘飨耢瑟瑚鹉瑁瑞瑰瑀瑜瑗瑄瑕遨骜瑙遘韫魂髡肆摄摸填搏塥塬鄢趔趑摅塌摁鼓摆赪携塮蜇搋搬摇搞搪塘搒搐搛搠摈彀毂搌搦摊搡聘蓁戡斟蒜蓍鄞勤靴靳靶鹊蓐蓝墓幕蓦鹋蒽蓓蓖蓊蒯蓟蓬蓑蒿蒺蓠蒟蒡蓄蒹蒴蒲蒗蓉蒙蓂蓥颐蒸献蓣楔椿楠禁楂楚楝楷榄想楫榀楞楸椴槐槌楯榆榇榈槎楼榉楦概楣楹椽裘赖剽甄酮酰酯酪酩酬蜃感碛碍碘碓碑硼碉碎碚碰碇碗碌碜鹌尴雷零雾雹辏辐辑辒输督频龃龄龅龆觜訾粲虞鉴睛睹睦瞄睚嗪睫韪嗷嗉睡睨睢雎睥睬嘟嗜嗑嗫嗬嗔鄙嗦嗝愚戥嗄暖盟煦歇暗暅暄暇照遢暌畸跬跨跶跷跸跐跣跹跳跺跪路跻跤跟遣蛸蜈蜎蜗蛾蜊蜍蜉蜂蜣蜕畹蛹嗣嗯嗅嗥嗲嗳嗡嗌嗍嗨嗤嗵嗓署置罨罪罩蜀幌嵊嵩嵴骰锖锗错锘锚锛锜锝锞锟锡锢锣锤锥锦锧锨锪锫锩锬锭键锯锰锱矮雉氲犏辞歃稞稚稗稔稠颓愁筹筠筢筮筻筲筼筱签简筷毁舅鼠牒煲催傻像躲鹎魁敫僇衙微徭愆艄觎毹愈遥貊貅貉颔腻腠腩腰腼腽腥腮腭腹腺腧鹏塍媵腾腿詹鲅鲆鲇鲈鲉鲊稣鲋鲌鲍鲏鲐肄猿颖鹐飔飕觥触解遛煞雏馌馍馏馐酱鹑禀亶廒瘃痱痹痼廓痴痿瘐瘁瘅痰瘆廉鄘麂裔靖新鄣歆韵意旒雍阖阗阘阙羧豢誊粳粮数煎猷塑慈煤煳煜煨煅煌煊煸煺滟溱溘滠满漭漠滢滇溥溧溽源滤滥裟溻溷溦滗滫溴滏滔溪滃溜滦漓滚溏滂溢溯滨溶滓溟滘溺滍粱滩滪愫慑慎慥慊誉鲎塞骞寞窥窦窠窣窟寝谨裱褂褚裸裼裨裾裰禊福谩谪谫谬群殿辟障媾嫫媳媲嫒嫉嫌嫁嫔媸叠缙缜缚缛辔缝骝缟缠缡缢缣缤骟剿耥璈静碧瑶璃瑭瑢獒赘熬觏慝嫠韬髦墈墙摽墟撇墁撂摞嘉摧撄赫截翥踅誓銎摭墉境摘墒摔榖撖摺綦聚蔫蔷靺靼鞅靽鞁靿蔌蔽慕暮摹蔓蔑甍蔸蓰蔹蔡蔗蔟蔺戬蕖蔻蓿蔼斡熙蔚鹕兢嘏蓼榛榧模槚槛榻榫槜榭槔榴槁榜槟榨榕槠榷榍歌遭僰酵酽酾酲酷酶酴酹酿酸厮碶碡碟碴碱碣碳碲磋磁碹碥愿劂臧豨殡需霆霁辕辖辗蜚裴翡雌龇龈睿弊裳颗夥瞅瞍睽墅嘞嘈嗽嘌嘁嘎暧暝踌踉跽踊蜻蜞蜡蜥蜮蜾蝈蜴蝇蜘蜱蜩蜷蝉蜿螂蜢嘘嘡鹗嘣嘤嘚嘛嘀嗾嘧罴罱幔嶂幛赙罂赚骷骶鹘锲锴锶锷锸锹锻锽锾锵锿镀镁镂镃镄镅舞犒舔稳熏箐箦箧箍箸箨箕箬算箅箩箪箔管箜箢箫箓毓舆僖儆僳僚僭僬劁僦僮僧鼻魄魅魃魆睾艋鄱貌膜膊膈膀膑鲑鲔鲙鲚鲛鲜鲟疑獐獍飗觫雒孵夤馑馒銮裹敲豪膏塾遮麽廙腐瘩瘌瘗瘟瘦瘊瘥瘘瘙廖辣彰竭韶端旗旖膂阚鄯鲞精粼粹粽糁歉槊鹚熄熘熔煽熥潢潆潇漤漆漱漕漂滹漫漯漶潋潴漪漉漩漳滴漾演澉漏潍慢慷慵寨赛搴寡窬窨窭察蜜寤寥谭肇綮谮褡褙褐褓褛褊褪禚谯谰谱谲暨屣鹛隧嫣嫱嫩嫖嫦嫚嫘嫜嫡嫪鼐翟翠熊凳瞀鹜骠缥缦缧骡缨骢缩缪缫慧耦耧瑾璜璀璎璁璋璇璆奭撵髯髫撷撕撒撅撩趣趟撑撮撬赭播墦擒撸鋆墩撞撤撙增撺墀撰聩聪觐鞋鞑蕙鞒鞍蕈蕨蕤蕞蕺瞢蕉劐蕃蕲蕰蕊赜蔬蕴鼒槿横樯槽槭樗樘樱樊橡槲樟橄敷鹝豌飘醋醌醇醉醅靥魇餍磕磊磔磙磅碾磉殣慭震霄霉霈辘龉龊觑憋瞌瞒题暴瞎瞑嘻嘭噎嘶噶嘲颙暹嘹影踔踝踢踏踟踬踩踮踣踯踪踺踞蝽蝶蝾蝴蝻蝠蝰蝎蝌蝮螋蝗蝓蝣蝼蝤蝙噗嘬颚嘿噍噢噙噜噌嘱噀噔颛幞幡嶓幢嶙嶝墨骺骼骸镊镆镇镈镉镋镌镍镎镏镐镑镒镓镔靠稽稷稻黎稿稼箱箴篑篁篌篓箭篇篆僵牖儇儋躺僻德徵艘磐虢鹞鹟膝膘膛滕鲠鲡鲢鲣鲥鲤鲦鲧鲩鲪鲫鲬橥獗獠觯鹠馓馔熟摩麾褒廛鹡瘛瘼瘪瘢瘤瘠瘫齑凛颜毅羯羰糊糇遴糌糍糈糅翦遵鹣熜熵熠潜澍澎澌潵潮潸潭潦鲨潲鋈潟澳潘潼澈澜潽潺澄潏懂憬憔懊憧憎寮窳额谳翩褥褴褫禤谴鹤谵憨熨慰劈履屦嬉勰戮蝥豫缬缭缮缯骣畿耩耨耪璞璟靛璠璘聱螯髻髭髹擀撼擂操熹甏擐擅擞磬鄹颞蕻鞘燕黇颟薤蕾薯薨薛薇檠擎薪薏蕹薮薄颠翰噩薜薅樾橱橛橇樵檎橹橦樽樨橙橘橼墼整橐融翮瓢醛醐醍醒醚醑觱磺磲赝飙殪霖霏霓霍霎錾辙辚臻冀餐遽氅瞥瞟瞠瞰嚄嚆噤暾曈蹀蹅踶踹踵踽嘴踱蹄蹉蹁蹂螨蟒蟆螈螅螭螗螃螠螟噱器噪噬噫噻噼幪罹圜鹦赠默黔镖镗镘镚镛镜镝镞镠氇氆赞憩穑穆穄篝篚篥篮篡簉篦篪篷篙篱盥儒劓翱魉魈邀徼衡歙盦膨膪膳螣膦膙雕鲭鲮鲯鲰鲱鲲鲳鲴鲵鲷鲸鲺鲹鲻獴獭獬邂憝亸鹧磨廨赟癀瘭瘰廪瘿瘵瘴癃瘾瘸瘳斓麇麈凝辨辩嬴壅羲糙糗糖糕甑燎燠燔燃燧燊燏濑濒濉潞澧澡澴激澹澥澶濂澼憷懒憾懈黉褰寰窸窿褶禧壁避嬖犟隰嬗鹨翯颡缰缱缲缳缴璨璩璐璪戴螫擤壕擦觳罄擢藉薹鞡鞠藏薷薰藐藓藁檬檑檄檐檩檀懋醢翳繄礁礅磷磴鹩霜霞龋龌豳壑黻瞭瞧瞬瞳瞵瞩瞪嚏曙嚅蹑蹒蹋蹈蹊蹓蹐蟥螬螵疃螳螺蟋蟑蟀嚎嚓羁罽罾嶷赡黜黝髁髀镡镢镣镤镥镦镧镨镩镪镫罅穗黏魏簧簌篾簃篼簏簇簖簋繁鼢黛儡鹪鼾皤魍徽艚龠爵繇貘邈貔臌朦臊膻臁臆臃鲼鲽鲾鳀鳁鳂鳃鳄鳅鳆鳇鳈鳉鳊獯螽燮鹫襄糜縻膺癍癌麋辫赢糟糠馘燥懑濡濮濞濠濯懦豁蹇謇邃襕襁臀檗甓臂擘孺隳嬷翼蟊鹬鍪骤鏊鳌鬶鬈鬃瞽藕鞯鞨鞭鞫鞧鞣藜藠藤藩鹲檫檵覆醪蹙礞礓礌燹餮蹩瞿瞻曛颢曜躇蹦鹭蹢蹜蟛蟪蟠蟮嚚嚣鹮黠黟髅髂镬镭镯镰镱馥簠簟簪簦鼫鼬鼩雠艟翻臑鳍鳎鳏鳐鳑鹱鹰癞癔癜癖糨冁瀑瀍瀌鎏懵襟璧戳彝邋鬏攉攒鞲鞴藿蘧孽蘅警蘑藻麓攀醭醮醯礤酃霪霭黼鳖曝嚯蹰蹶蹽蹼蹯蹴蹾蹲蹭蹿蹬蠖蠓蠋蟾蠊巅黢髋髌镲籀簸籁簿鳘齁魑艨鼗鳓鳔鳕鳗鳙鳚蟹颤靡癣麒鏖瓣蠃羸羹爆瀚瀣瀛襦谶襞疆骥缵瓒鬓壤攘馨蘩蘖蘘醵醴霰颥酆耀矍曦躁躅蠕鼍嚼嚷巍巉黩黥镳镴黧籍纂鼯犨臜鳜鳝鳞鳟獾魔糯灌瀹瀵譬孀骧耰蠢瓘鼙醺礴礳霸露霹颦曩躏黯髓鼱鳡鳢癫麝赣夔爝灏禳鐾羼蠡耲耱懿韂蘸鹳糵蘼囊霾氍饕躔躐髑镵镶穰鳤瓤饔鬻鬟趱攫攥颧躜罐鼹鼷癯麟蠲矗蠹醾躞衢鑫灞襻纛鬣攮囔馕戆蠼爨齉"
]

def printCharData(filename):
    DOMTree = xml.dom.minidom.parse(filename)
    nameCollection = DOMTree.documentElement.getElementsByTagName('name')
    print('字体信息：')
    for nameElement in nameCollection:
        nameId = int(nameElement.getAttribute('id'))
        nameValue = nameElement.getAttribute('value')
        print('    %s 的值：%s' % (nameIdList[nameId], nameValue))
    glyphCollection = DOMTree.documentElement.getElementsByTagName('g')
    glyphLength = glyphCollection.length
    glyphList = []
    for i in range(glyphLength):
        glyphElement = glyphCollection[i]
        if not glyphElement.hasAttribute('u'):
            glyphName = glyphElement.getAttribute('n')
            print('\033[K没有 Unicode 编码的字符 %s，省略' % glyphName)
        else:
            glyphList.append(int(glyphElement.getAttribute('u')))
            print('\x1b[s\x1b[K读取字形…（%3.0f%%）\x1b[u' % (i / glyphLength * 100), end='')
    print('%d 个编码字符' % len(glyphList))
    charsetName = ['通规一级', '通规二级', '通规三级', '国标一级', '国标二级', '现汉通']
    charsetList = 通用规范汉字表字表 + 基本集字表 + 现汉通字表
    missingGlyphsAll = ''
    for i in range(len(charsetList)):
        charset = charsetList[i]
        havingGlyphsSet = ''
        print('\n匹配字表 %s（第 %d 个）：' % (charsetName[i], i + 1))
        for j in range(len(glyphList)):
            glyphChar = chr(glyphList[j])
            if glyphChar in charset:
                havingGlyphsSet += glyphChar
        missingGlyphsSet = ''.join(set(charset).difference(set(havingGlyphsSet)))
        if len(missingGlyphsSet) == 0:
            print('（空）')
        else:
            print(missingGlyphsSet, '（共 %d 个）' % len(missingGlyphsSet))
        missingGlyphsAll = ''.join(set(missingGlyphsAll).union(set(missingGlyphsSet)))
    print('\n总的缺失字符：\n%s（共 %d 个）' % (missingGlyphsAll, len(missingGlyphsAll)))

printCharData('MuzaiPixel.kbitx')