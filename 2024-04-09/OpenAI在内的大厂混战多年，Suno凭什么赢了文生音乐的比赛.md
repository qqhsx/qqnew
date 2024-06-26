# OpenAI在内的大厂混战多年，Suno凭什么赢了文生音乐的比赛

[](https://news.qq.com/omn/author/8QMZ3XxU64wZuTw%3D)

[腾讯科技](https://news.qq.com/omn/author/8QMZ3XxU64wZuTw%3D)

2024-04-09 06:30发布于河北腾讯新闻科技频道官方账号

![图片](https:https://inews.gtimg.com/news_bt/OMFF0w5JU416pBR9KDsqQvb9SBn1-8v2OynhF23holTZkAA/641)
文 / 腾讯科技 郝博阳 周小燕

Suno V3让音乐行业迎来了“ChatGPT时刻”。

它一经问世，便引发音乐行业“震动”，其中一个原因是Suno V3占据C端属性的天然优势，它令音乐创作变得更简单。

Suno V3十分“亲民”，用户可以“傻瓜式”操作，只要用Suno V3输入文字，就能获得一曲完整的、带人声的歌曲。我们曾详细体验，Suno
V3如何令五音不全的音乐“小白”制作出一首像模像样的歌曲：“小白”一脚踹进“音乐圈”？年轻人靠Suno“搞钱”还差几步

你既可以输入简单的一句话来生成音乐，比如输入Prompt：在阳光下，一群18岁的少年欢快地唱着歌，用中文唱

就能获得一首带有人声的歌曲，充满青春气息的女声，热情地歌唱：

#### 按住画面移动小窗

X

也可以尝试专业音乐人的路子，输入Prompt：

风格：现代流行摇滚

调式：大调

节奏（BPM）：95 BPM

结构：传统Verse-Chorus，带有创新桥段

旋律：简单易记，情感丰富

和声：丰富流畅

鼓组：融合摇滚鼓与电子鼓点

人声效果：远程混响和轻微自动调节音

乐器：电吉他、贝斯、鼓，加键盘或合成器

目标：触动人心的流行摇滚作品，结合情感深度和感触

你可以获得一首这样的歌曲：

#### 按住画面移动小窗

X

看上去操作简单的步骤，实现起来并不容易。因为做一款“Text-to-
Music”会面临更复杂的技术挑战和用户审美挑战，这也是为什么相比较于其它与AI结合的媒介，音乐显得有点“掉队”的原因。

在过去几年里，Midjourney、Sora的出现，令“Text-to-Image”（文生图）、“Text-to-
Video”（文生视频）都分别抵达自己的“ChatGPT时刻”，而属于音乐的ChatGPT时刻却迟迟未来。其实，大厂们其实一直都在积极探索AI音乐赛道：

2020年4月，Open
AI就公布了深度学习生成音乐的产品JukeBox，它通过分析大量的音乐数据，不仅会生成旋律，还能生成对应的歌词，模仿多种不同的艺术家和音乐风格。

2023年，谷歌开始密集公布关于其AI生成音乐项目MusicLM的论文和研究。

同一段时期内，Meta也不断公开其关于AI音乐的项目和研究，主要成果有关注专业AI音乐生成的MusicGen、AI生成环境音的AudioGen，以及EnCodec。

虽然大厂们在持续探索，但音乐行业的ChatGPT依旧姗姗来迟，这或许与人类对不同介质的敏感度有关。给你一张AI生成的图片，未必能挑出它的毛病，但如果给你一段AI生成的音乐，或许很快就能发现其中的不和谐。

不论是图像还是视频，调动的都是人类的视觉能力，而人们往往对视觉信息有更高的宽容度，相比之下，听觉系统对音频的细微变化却有着较高的敏感度，音乐的节奏、旋律、和声等细微的变化，都会影响受众对音乐质量的判断。

尽管Suno
V3的出现将AI生成音乐带到了新的阶段，但与文字、图像、语音这些诞生了OpenAI、Midjourney、11Labs这样的头部初创公司赛道相比，音乐依旧慢了半拍，就连视频这一被业内公认最难突破的赛道，也随着今年年初Sora的出现，迎来了属于自己的ChatGPT时刻。

“音乐”这个看似复杂性远低于视频的赛道，却在Suno的姗姗来迟之下，才跨过了这道坎儿，做一款音乐版ChatGPT，到底面临哪些难点？

音乐生成发展史：大厂全入局，跑出来的却是初创公司

人们用神经网络探索AI生成音乐的历程，并不比AI生成文字或AI生成图片短，而且，AI生成音乐的路子，一开始就走得很“正”。

又是谷歌开天辟地

2014年，ImageNet让全世界见识到了深度学习的能量，2016年，谷歌通过Megenta项目正式将音乐生成领域带入神经网络时代。

一开始谷歌还尝试通过一些传统的方法诸如RNN、GAN来生成音乐，到了2018年，谷歌就把Transformer架构应用到了音乐生成上，发布了Music
Transformer，而此时距离Transformer论文发布仅仅相隔一年。

引入Transformer架构之后，
AI生成音乐顿时变得近在眼前。过去，基于LSTM（RNN）的音乐生成只能保证音乐在几秒左右不跑偏，而擅于生成长结构的Transformer，却可以直接将音乐“不跑偏”的时长拉到2-3分钟。虽然在结构性上，AI生成的音乐依旧无法媲美人类编曲，会出现较为严重的重复现象，但音乐的规律性和连续性却可以得到保障。谷歌的成功，在文字之外开启了音乐生成学术层面的“狂飙时刻”。

#### 按住画面移动小窗

X

不久后，另一个Transformer信徒OpenAI也很快跟进，在GPT-2刚刚发布的2019年，OpenAI就同期发布了MuseNet，它和GPT-2都使用了Transformer架构的音乐生成模型。相对于只能生成MIDI古典钢琴曲的Music
Transformer，虽然MuseNet训练集依然是音色简单的MIDI合成乐，但它可以使用10种不同的乐器生成长达4分钟的音乐作品，并且在音乐风格上，可以顺畅实现从乡村音乐到莫扎特，再到披头士乐队风格的切换。

比起Music Transformer，MuseNet使用了更擅长处理上下文的Sparse
Transformer（稀疏Transformer)，这让音乐的生成更具有连续性。

MuseNet专门为处理音乐增加了几个新的嵌入维度，并增加了模型的时间流通性和结构性，这让其所生成的音乐从“随机化”转为更具备“结构性”，甚至更有“发展性”。

https://soundcloud.com/openai_audio/jazz-trio

![图片](https:https://inews.gtimg.com/news_bt/O6-X7SytOzQLwBYSR5PFDvjDCkA8_VLUN0gdOFmozxDmYAA/641)
（黑色为非神经网络模型，蓝色为神经网络模型）

在这一阶段，由于Transformer本身出色的架构，音乐的结构和旋律的一致性得以保存，但因为缺乏对长音乐跨度的掌握，音乐内段落的重复感很强。

OpenAI确立标准，引入人声

在这个阶段，虽然音乐生成已经成功，但算力和模型本身的限制，让训练只能开展在简单的MIDI音乐基础上。

比起MuseNet这种用MIDI合成音训练出来的音乐，OpenAI想要还原更真实，更丰富的音乐。

2020年，由OpenAI首席科学家Illya带队发布的JukeBox，给Transformer架构加上了一个更适合音乐的压缩编码机制，这奠定了Transformer文生音乐的基本架构。

与文字生成不同，多模态模型在训练中的原始内容和信息更多。比如，一首典型的CD品质的4分钟歌曲（44 kHz，16
位）有超过1000万个时间步，如果全部转换成token，现有的算力根本顶不住。为了能处理更复杂的原始音乐，需要一个“压缩”步骤来加快运算和推理。同时这种压缩还有另外一个好处：模型可以掌握到更多的长程信息，形成对旋律结构的深入理解。

在JukeBox中，OpenAI选择的压缩编码机制是VQ-
VAE机制，这是一个可以把原始音乐分成从复杂到简单的三层结构：分别为8倍，32倍，128倍。模型通过最上面的抽象层，可以学到一段音乐里每个“24秒”所呈现出的结构，在最下一层只能学到每个“1.5秒”之间音乐的关系。这样分别训练不同层级的压缩，结构和细节数据就全获得了。

![图片](https:https://inews.gtimg.com/news_bt/OAD8C9q150BceUqga1xMKIidOTJy-S4WIkWu9lD2ycgewAA/641)
（VQ-VAE的三层模型）

压缩技术让Jukebox能够更好地理解音乐文本，即长旋律。除此之外，OpenAI还在加了人声，让整个歌曲变得完整。

而在这之前根本没有过将人的歌声和旋律对位的方法，OpenAI仅仅用了一个简单的方式，就将人声的每个单词和音乐分开作为原素材训练模型，结果获得了成功。为了更好地实现对齐，OpenAI还给歌词加了个更高编码层，并额外嵌入了歌词的信息，对应艺术家和风格的信息等，让模型更容易生成符合歌词逻辑的歌曲。

这和我们现在经常听到的“AI孙燕姿”不同，“AI孙燕姿”其实是一项Converter的技术，即利用AI去对位的新声音特性，覆盖旧歌曲的音色。而Open
AI的这项人声技术根本不需要理解音乐结构。

从结果上来看，人声唱歌这部分的问题，从词曲对位，发音和音调符合角度讲，OpenAI基本都解决了。缺乏的就是更好的音色和更准确、清晰的合成人声了。

但有趣的是，也许是OpenAI把问题解决得太彻底了。所有除了Rifussion和Suno之外，后面的音乐模型，都没有再在其基础模型中加入人声了。

https://soundcloud.com/openai_audio/count2

在这一阶段，OpenAI解决了原始素材和人声生成的问题，现在他们可以从更广阔的现实音乐中去获取训练素材，而不用只守着MIDI库了。而且通过压缩，它在一定程度上更好地解决了生成音乐的结构复杂度问题，只是在此基础上略微有所泛化。虽然它合成的声音虽然到了45khz，但还比较粗糙，音色上并不清晰。

Google引入文生音乐，Meta加入战局

包括Jukebox在内，所有2022年之前的音乐模型都是Premater-
based，即给定一些条件（如音乐类型，相似音乐家），然后由AI去生成。但2023年，GPT-3引发的文生文模型的大发展，让Prompt引导的文生音乐应运而生。最先走向这个模式的，是2022年发布的Riffusion，后面就是Google在2023年1月发布的MusicLM。

![图片](https:https://inews.gtimg.com/news_bt/OQGRboPoy4vSmhranIuXTk2iHt311qwx7tMm1qMz37AE8AA/641)
https://google-
research.github.io/seanet/musiclm/examples/audio_samples/long_generation/relaxing-
jazz.wav

MusicLM搭建在Google之前发布的语音模型AudioLM之上，并在上面加上了一个从文到音乐的映射架构MuLan，这本身就是个基于有标注的音乐去判定无标准音乐相对应描述文字的系统。AudioLM本身由两个部分组成，一个是负责理解音乐语义，也就是长程结构和旋律的w2vBERT去生成语义token；另外一个部分是SoundStream，它负责生成音色token，去丰满语义部分的结构。

这听起来和JukeBox的不同压缩层如出一辙，但AudioLM并非端到端的模型，而是一个流水线（Pipeline）：Mulan接收语义，w2vBERT映射出旋律，再结合语义让SoundStream生成对应的音色。

JukeBox生成的音乐虽然结构更好，但音色不灵，经常出现奇怪的合成音。对此，Google在做了两项升级：

一是SoundStream用RVQ这一新技术取代了OpenAI用的VQ-VAE压缩机制，RVQ本身只是VQ-
VAE的一个变体，在VAE的过程中，音色从被压缩到被还原中间的损失非常大，RVQ就通过一种包含了多种声音延展规律的CodeBook（编码本）拟合这中间的差值。

同时，为了同时达成音效和结构的最优化，MusicLM干脆就将结构和音色分开处理，它分别用w2v-Bert单独处理结构，SoundStream单独处理音色。这导致MusicLM最终生成的音乐确实比JukeBox更加清亮还原，也能保持一定的结构一致性。

2023年6月，Meta也加入了文生音乐的大军，它推出了AudioCraft系列产品，包括负责生成音效的AudioGen，生成音乐的MusicGen以及一个全新的压缩编码方式Encodec。

Meta推翻了Google的分阶段流水线，在MusicGen里直接用已有的文字和音乐对应的编码器T5作为文字音乐对应的基础，把它加入到整个模型的训练中。由此回归到了由OpenAI开创的大一统Transformer+压缩机制，直接端到端，形式简单。

MusicGen的整体模型和谷歌的SoundStream很相似，也是用一个框架Transformer联合RVQ，在这里被Meta称为Encodec压缩。比起谷歌，Meta还特意对CodeBook（编码本）做了升级，用多种Code模式交织辅助生成。加用了更细致的音频处理方法(如多分辨率频谱损失)，因此在压缩后的音频质量上有更优的表现。这使得模型能更好地捕捉原始音频中丰富的音色、质感等细节，使重建后的音频更加自然逼真。

![图片](https:https://inews.gtimg.com/news_bt/OQkmTTC1fFtaq0Ac82qtyRsCZbljo13W9-sGC2dl9Y6V0AA/641)
![图片](https:https://inews.gtimg.com/news_bt/OCRicJe8X-XT3Xettq2Z_K9WazXNpJ7hSt3GeEC4uS3SQAA/641)

（MusicGen的架构和四种常见的Codebook排布）

到了这一阶段，音乐生成的主要进展有了更贴近用户使用习惯的文本Prompt模式，另外在音色生成上靠着新的压缩方法有了新突破。通过更大的算力、更好的压缩机制，生成时间也大为缩短。在Jukebox时期，生成一分钟的曲目需要9个小时的推理，但在MusicLM时代，这一过程只需要十几秒。

在训练和模型参数水平上，MusicGen和MusicLM的训练集都扩展到了20万-30万小时，足足有JukeBox的五六倍；模型也有了相较于2020年更大的参数（MusicGEn的参数有30亿，相比文生文很小，但在音乐领域算比较大的）。

这都使这些模型还原更精确，扩展到的音乐类型更多，泛化也更强。但有个基础问题还是没有解决，就是长结构的问题。

这一问题在另一派以Stable Diffusion为基础的模型中更为突出。

另一派：Stable Difussion生成音乐，长于音色，困于长度

在文生图领域一直处于统治地位的Stable
Difussion（扩散模型），也在音乐生成中走出了一条自己的路。和图像生成一样，Diffusion的结构让音乐生成的音质一骑绝尘，但和它在视频生成领域的表现一致，不管是谷歌在2023年2月发布的Noise2Music模型，还是在九月Stability发布的Stalbe
Audio，Diffusion模型对结构和上下文的理解简直一塌糊涂。这一模型虽然能依靠联级Diffusion生成30秒以上的音频，但其结构和和声对位都过分天马行空，难以控制，各种突然冒出来的音此起彼伏。

https://google-research.github.io/noise2music/table1/wavegen_8.wav

这其中做的最好的，经过多次迭代的Riffision，也只能保证在12秒生成的音乐中保持旋律的一致性和发展。当然，它的音质效果完全超越了Transformer基础的模型，提供了当前最接近“成品音乐”的质感。

https://riffusion.com/riffs/6fb593c6-f4f6-42ac-9da9-388367401ea1

Suno到底赢在哪里？

从技术上解决了文生音乐的最后一道大坎

通过梳理文生音乐的发展史，我们看到在MusicGen这个时间点上，文生音乐的所有基础能力都集齐了：音色问题解决的差不多了，短旋律拟真度也很高，和声部分足够丰富，生成速度也很快。乍听起来，它们生成的音乐段落和Suno的纯器乐没什么明显不同。

而Suno也是结结实实的站在巨人的肩膀上，在它踏入文生音乐领域之前的基础模型Bark中，Suno明确列出了这一模型的核心原理基础：全是Meta和Google的老朋友们。

![图片](https:https://inews.gtimg.com/news_bt/OBLd7N0k__MmRqEAs6VX32kjIgX89wFq8u2l7_aNYMuWQAA/641)
然而，在这个时间点上，从一开始就困扰着OpenAI的音乐”上下文“——长结构问题仍然没有解决。

在OpenAI在对JukeBox的技术报告中说到，”虽然生成的歌曲显示出本地音乐的连贯性，遵循传统的和弦模式，甚至可以具有令人印象深刻的独奏，但我们没有听到熟悉的较大音乐结构，例如重复的合唱。“

不论是MusicLM还是MusicGen，其生成的音乐语义结构理解基本都基于30s左右的样本长度窗口，就算是MusicLM专门用于理解长结构的w2vBERT也一样。超过这个长度就只能依靠前端作为引子，基于前10s再继续生成。这使得这些模型虽然都能生成超过3分钟的长音乐，但根本不可能理解长过30s的音乐结构。

而我们日常听的歌曲基本都是三分钟以上为长度单位的，最少也要1分半钟以上才能有较为完整的结构。在现代流行音乐中，我们一般把一首音乐分为引子、主歌、副歌、桥接部和结尾，加在引子之后的就是各种主幅歌以ABAB、ABCA之类的排列的结构。只有满足这样的结构，我们才能觉得一首曲子有始有终，有发展有高潮。

过去文生音乐模型完全不可能建构出这样的完整曲式，因为它没见过。因此，在Suno之前，我们都只能说AI在生成一个片段，就算是它生成的是3分钟的音乐，也不过是一堆片段，而非整首歌曲。

![图片](https:https://inews.gtimg.com/news_bt/OrMgluAb-k18xv_CHduzOjWxJfzL9ApuVG9JlPIoNIySYAA/641)
但Suno 解决了这个问题。它能做到引子+主歌+副歌+结尾的至少1分半才能完成的完整结构。AI第一次能生成歌曲，而非音乐片段了。

Suno从去年9月开始到今年3月一共迭代了三个版本，从其第一个版本开始（那时这个产品还叫Chrip）就已经具有了完整结构，后两次迭代更新主要是进一步优化提升音质。

![图片](https:https://inews.gtimg.com/news_bt/OomtyeZhE-cLks4iLpvi1c52lpx-9O73dJbtcUJyD_jBkAA/641)
（Suno默认的歌词生成，带有主歌和副歌结构）

Suno是依靠什么做到前人都没做到的程度的？这一点由于Suno三代产品都未开源，我们没法确知其具体方法。但它从6月开始由生成语音的Bark转向生成音乐的Chrip，3个月时间就完成了大厂花了5年都没完成的突破。说明也许解法并不复杂。

比如可以预见的简单思路是：

1）把训练窗口提高到30s以上，这样模型见过结构了，就可能理解泛化出结构。

2）再通过对生成进行一定的结构嵌入，或通过instruction要求保持结构。但这一步必须得要在1的前提下才有可能。

当然，也许换个更强的模型也能解决这个问题。Stable Difussion 近期刚刚用最流行的Diffusion
Transformer（DiT）模型升级了自己的文生音乐模型Stable Audio 2，它的结构属性就比上代强出不止一点半点。

https://stableaudio.com/1/share/db8f02a4-6be3-4528-9f85-6f32d745bccd

产品全力toC，直冲爆款而来

技术功不可没，但Suno优秀的产品嗅觉也不能忽视。相比于市面上的竞品，它的产品设计就是全力ToC，各方面都直指爆款：

1、支持人声，赢得大众

对于大众来讲，能生成歌曲，而非纯音乐才是他们的真需求。这是因为歌词能传递的东西更直接。一句“谢帝我要迪斯尼”的表达比一首trap
beat更容易理解，也更有传播度。想要ToC火起来，能生成人声歌唱是必须的。加了人声歌词，文生音乐才对大众而言“可玩”。

但在Suno之前，他的主要竞品除了Riffusion的12秒歌词外，其他的都只能生成纯音乐。

从OpenAI在Jukebox的尝试里看，生成人声歌唱并没有那么高的技术门槛。Suno的竞品之所以不做，主要是出于两个理由：

1）对于大厂而言，人声生成可能能追踪到训练集，侵权风险高，干脆算了。

2）对于竞品产品而言，现阶段他们认为AI文生音乐还没到技术成熟期，toC推不开，不如专注toB，先有收入。

但Suno作为一个初创公司，既没有大公司的顾忌，又有toC的技术底气，加就加了。再加上他们第一个产品Bark本来就是人声生成，看家本领怎能不用，这就有了它能火的第一个要素。

2、界面傻瓜式生成，但给够一半用户玩的空间

因为toB，面向的是专业团体，所以Aiva，Loudly都干脆还在利用风格之类的标签生成音乐，界面也很专业复杂，甚至还支持专业的调音系统，这对于一般用户来讲都不怎么友好。

![图片](https:https://inews.gtimg.com/news_bt/ODV0iDJwq88UI9HjPNRhOrERiS2aEojMqStwM_j3S1dZkAA/1000)
（Avia的用户界面，直接能转到调音台）

但Suno本身的界面简单到爆，一个框输入prompt就可以，一键生成。为了防止你对这种只能输入偏曲风向的prompt感到厌倦，它还设置了自定义模式，多了可以输入歌词的位置。这对于专业人士来讲可能意义有限，但对一般大众，歌词才是最大的可玩性。也是靠着这项功能，才会有《连花清瘟》之类的Suno神曲在它上线时刷屏全网。

想要C端自传播，不能难，还要得能留下让大家很快能玩出花的空间。

![图片](https:https://inews.gtimg.com/news_bt/OjGNcFpgDfxQYaeS0HB3vlyC8Vy418FxVg76yhe024loQAA/641)
3、作品画廊，神器摇篮

虽然MusicLM和Refussion、Stable Audio的
界面相对比较简洁，但除了不能有人声支持和歌词自定义玩法之外，他们还缺了“作品画廊”这个引发自传播的经典产品模块。

在这里，你可以看到全曲只有Cat（猫）歌词的曲子，也能看到”人工智能搞掉了我的工作“这样的一眼就想点，听了就想转的神曲。这样的神曲在过去很少，因为音乐制作成本太高，谁会用音乐来整活儿。但现在可以了。Suno揭开的是真的音乐“娱乐”时代。

Suno创始人曾在访谈中表示，每天登录网站的人中，听歌的人比真的去生成音乐的人还多。

这既说明了这些“神曲”受欢迎，被转发的程度之高，也说明了作品画廊的拉新能力之强。

![图片](https:https://inews.gtimg.com/news_bt/ORcpoRkdYjb2T_WVthzQzBUr_fTN2GlwKRXuIO09v3iigAA/641)
https://app.suno.ai/song/ee467d00-5813-4a74-9792-c9ae4a09d344

Suno的出现，将如何改变市场和这个时代？

每出现一款类似的产品，都可能会改变一个行业原有的格局与产业链，Suno V3对不少音乐从业者而言也是一名“搅局者”。

在2023年，已经有了将近50家公司依靠着音乐生成技术在市场上获得了生存空间。基于他们各自音乐生成的产品定位，技术强项等，每家公司都有了一个相对细分的市场定位，形成了一种较为复杂的市场生态。但Suno
V3的出现直接掀了桌。

著名风投机构a16z根据目标群体，对AI音乐产品做了分类，以Royalty-Free music（免版税曲目）为分界线，在下面这张图中：

左半边代表AI对音乐产业的改造，让普通人也可以通过AI工具创造音乐；

右半边代表AI给专业的音乐从业者带来的工具变化。

![图片](https:https://inews.gtimg.com/news_bt/OR3joXQsKu3ExnOYeMLbFevJI1upaMgLvyNmRNsFLchxEAA/641)
（来源：a16z）

对普通人而言，AI音乐主要经历了两个阶段，第一个阶段是以Spotify为代表的“实时音乐流媒体”，还有Endel、Brain.fm和Aimi，它们会生成可以无限循环的音乐播放列表，帮助用户沉浸在特定的情绪之中。2023年2月，Spotify推出AI
DJ，用户可以使用AI DJ来生成精选音乐，它可以基于用户听过的历史音乐、根据用户反馈来不断更新曲目。

第二个阶段是“AI翻唱”，类似的产品有Musicly，
Voicify，Covers以及Kits等，用户可以通过上传自己或其他人的歌曲片段来转换声音。根据a16z报道，自从“Heart On My
Sleeve”上线以来，AI翻唱行业出现了爆炸式增长，标有#AICover的视频在短视频平台上的播放超过了100亿次。

对于专业音乐从业者而言，AI音乐起始于免版税曲目（又叫做AI
Muzak），它帮助早期的个人内容创作者和中小企业实现在音乐制作过程中，达到质量和成本之间的平衡。这类产品有Beatoveb、Soundraw和Boomy等，用户可以使用这些工具选择流派、情绪等，然后自动生成曲目。

AI
Muzak之后，最令人瞩目的便是大模型与音乐的结合，相比较于前几个阶段的“傻瓜式”操作，在这个板块，音乐人可以通过工具来发挥专业化的技能，每个音乐创造的环节都能使用相应的工具，比如生成样本可以使用Soundry
AI 、旋律 软件MelodyStudio 、MIDI文件Lemonaide、AudioCipher等，甚至混音工具RoEx.

![图片](https:https://inews.gtimg.com/news_bt/ONE4KJjh4NiHosoyGg7P5dNlyv9JZEITjHsR0N0ZISViMAA/641)
（来源：a16z）

按照a16z的划分框架，Suno
V3的能力其实跨越了从Consumer到Professional之间几乎所有生态，它既可以给C端用户提供音乐创作便捷，通过插件安装未来或许也能够成为专业人士的创作工具。

那Suno V3和所有这些AI辅助创作工具能给这个时代带来些什么吗？

也许是一些过去沉默声音的浮现。

最近B站突然掀起了一股猫Meme+文字的创作风潮。创作者利用一些现成的表达一些感绪状态的猫咪梗图搭配文字去叙事。

相对于传统的视频形式，这种视频的制作成本极低，又有着足够丰富的表达元素和观看趣味性。因此很多过去不进行内容创作的用户开始尝试利用猫Meme视频进行日常生活，亲身经历的演绎。

在这种简单形式的加持之下，很多过去不知道如何表达的人讲出了他们其实非常有价值的故事，也获得了观众的接受，诞生了许多百万播放的爆款。

![图片](https:https://inews.gtimg.com/news_bt/OZESO7lLfSesJJoxz7NsWClLnMIxAKWKcfKgZeDTVp3GMAA/1000)
更值得注意的是，在猫Memo中，有很多受创伤的，很私人的故事被表达了出来。这样的创伤故事在过去单纯的文字语境下是非常难以表达的，但是在萌猫的簇拥之下，它被去伤痛化，获得了表达的权利。也更容易被大众所接受。

这就是形式本身的力量。一件件难以言说之事，一桩桩看看寻常的事变得动人，变得让叙述者觉得值得去表达。因为他们本来其实没那么寻常，而是富有力量的。

音乐也是这样一种可以让沉默之声响亮起来的形式。

对于一个普通人而言，他欣赏音乐的品味和制作音乐的能力之间可能有着巨大的差距，这一点Suno创始人Mikey
Shulman也非常认可，他在接受采访时直言：“我喜欢音乐，但我是一个有抱负的平庸的音乐家，我会用非常平庸的方式弹奏吉他”。

从Suno v3开始，人类创作的某些形式限制继图像，文字和视频之后又被打破了。在各个社交媒体上，我们已经看到了很多用AI生成的，歌唱自己个人心声的歌曲。

人类正式进入了AI开创的所有传统形式都表达丰盈的时代，我们也可以听到更多这样的故事。

  *  ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

  * ______

查看原图 547K

  * ![](https:https://inews.gtimg.com/news_bt/OMFF0w5JU416pBR9KDsqQvb9SBn1-8v2OynhF23holTZkAA/641)
* ![](https:https://inews.gtimg.com/news_bt/O6-X7SytOzQLwBYSR5PFDvjDCkA8_VLUN0gdOFmozxDmYAA/641)
* ![](https:https://inews.gtimg.com/news_bt/OAD8C9q150BceUqga1xMKIidOTJy-S4WIkWu9lD2ycgewAA/641)
* ![](https:https://inews.gtimg.com/news_bt/OQGRboPoy4vSmhranIuXTk2iHt311qwx7tMm1qMz37AE8AA/641)
* ![](https:https://inews.gtimg.com/news_bt/OQkmTTC1fFtaq0Ac82qtyRsCZbljo13W9-sGC2dl9Y6V0AA/641)
* ![](https:https://inews.gtimg.com/news_bt/OCRicJe8X-XT3Xettq2Z_K9WazXNpJ7hSt3GeEC4uS3SQAA/641)
* ![](https:https://inews.gtimg.com/news_bt/OBLd7N0k__MmRqEAs6VX32kjIgX89wFq8u2l7_aNYMuWQAA/641)
* ![](https:https://inews.gtimg.com/news_bt/OrMgluAb-k18xv_CHduzOjWxJfzL9ApuVG9JlPIoNIySYAA/641)
* ![](https:https://inews.gtimg.com/news_bt/OomtyeZhE-cLks4iLpvi1c52lpx-9O73dJbtcUJyD_jBkAA/641)
* ![](https:https://inews.gtimg.com/news_bt/ODV0iDJwq88UI9HjPNRhOrERiS2aEojMqStwM_j3S1dZkAA/1000)
* ![](https:https://inews.gtimg.com/news_bt/OjGNcFpgDfxQYaeS0HB3vlyC8Vy418FxVg76yhe024loQAA/641)
* ![](https:https://inews.gtimg.com/news_bt/ORcpoRkdYjb2T_WVthzQzBUr_fTN2GlwKRXuIO09v3iigAA/641)
* ![](https:https://inews.gtimg.com/news_bt/OR3joXQsKu3ExnOYeMLbFevJI1upaMgLvyNmRNsFLchxEAA/641)
* ![](https:https://inews.gtimg.com/news_bt/ONE4KJjh4NiHosoyGg7P5dNlyv9JZEITjHsR0N0ZISViMAA/641)
* ![](https:https://inews.gtimg.com/news_bt/OZESO7lLfSesJJoxz7NsWClLnMIxAKWKcfKgZeDTVp3GMAA/1000)

