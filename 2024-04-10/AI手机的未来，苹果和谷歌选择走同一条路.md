# AI手机的未来，苹果和谷歌选择走同一条路

[](https://news.qq.com/omn/author/8QIf3n9U6YMVuT%2FQ4ws%3D)

[AI未来指北](https://news.qq.com/omn/author/8QIf3n9U6YMVuT%2FQ4ws%3D)

2024-04-10 19:16发布于北京腾讯科技AI未来指北官方账号

![](https://inews.gtimg.com/news_bt/OmhjR-8HULgVsFf1cZ2HBPQC7U_UJN_RBY3Q9jACxODiUAA/1000)
文/腾讯科技 郝博阳

离WWDC还有两个月，苹果的“AI大计划”也越来越清晰了。

![](https://inews.gtimg.com/news_bt/OOKJu5jhdFi5Us8SnDbHUkc_IVfXuDqDulMjDTMoNNKRgAA/1000)
4月9日，苹果发布了一篇最新的论文，推出了一个叫Ferret-UI的新模型。这一模型的技术本身并不复杂，但是它所指向的是一场真正的手机AI革命。

在AI异军突起的2023年，很多人都在猜测生成式AI会对智能硬件市场带来什么变局。甚至怀疑智能手机还能否适应AI时代的新交互模式。

也由此应运而生了Rabitt R1， AI Pin等多种所谓AI
native的硬件。他们通过更好地利用了AI的交互特性和Agent能力试图挑战智能手机的霸权，用取消手机的方式去替代手机。

反观智能手机一侧，却只能以功能寥寥的端侧模型，可有可无的应用来做无力的反击。其霸主苹果甚至一度被认为完全落后于AI时代。

**但现在它回到了主场，还准备好了智能手机可能用来面对AI时代的答案：AI Native的手机系统。**

苹果发了篇新论文，漏出了它的整套计划

这次苹果新发布的Ferret UI是建立在苹果在其Ferret 多模态模型之上的。

相较于其他多模态模型，Ferret在发布时展示出的主要长项是对于图像具体区域和定位点的认知远远强于其他多模态模型，包括GPT4ROI。

在这个模型里，苹果提出了一个有着图像编码器、空间感知的视觉采样器和语言模型（LLM）的新架构。它有能力够处理不同形状之间的稀疏性差异，因此可以分辨出来自区域的形状（比如点、线和边框）。用户可以基于画面中具体的区域与大模型展开更深入的对话。

![](https://inews.gtimg.com/news_bt/OjJQQCuN7hEzqNIYLqPuxzZiBZO7buANvbZh1B6QzQf08AA/1000)
Ferret在十月刚刚发布时，业界对其反响并不热烈，一来因为它的区域识别长处并非当时大模型领域所最关注的问题，二来它只有7B和13B两个大小，相对于主流大模型太小了。10月中，硅谷的模型公司还在卷上下文，行内只把它当成苹果在大模型上的一场试水。

但随着Ferett UI的推出，Ferett的定位和目标就显得清晰多了：它就是苹果准备在新IOS上装载的模型，至少是其中一个主要模型。

![](https://inews.gtimg.com/news_bt/OxK210I-pGSIAHnBiJ7zLpk0H7yfPzyL_6Xrun4-MZTHIAA/1000)
Ferett
UI所做的事情就是将Ferett模型本来就很强大的图片区域识别能力应用在手机UI之中，通过优化，使它能够更好的识别手机应用的界面。并将自然语言翻译为界面操作点。

简单来讲，就是当你和AI去聊关于手机界面的情况时，它能懂你在说什么，并找到具体的元素了。

在之前，多模态大模型（MLMM）去理解手机UI经常会出现错误。这主要是因为：

UI界面通常具有更长的纵横比 ，基于正常图片（16:9 / 4:3）训练的大模型无法抓住其图像全貌。

并且包含许多小的感兴趣对象(如图标和文本)，直接应用现有模型可能会丢失理解UI界面所需的重要细节。

为解决UI不常见的问题，Ferret-UI以Ferret模型为基础，在其上集成了"any
resolution"(anyres)技术来灵活适应各种屏幕纵横比。整个流程如下:

UI界面大，那就把它分割成几个小的子图像，以更好地捕捉UI界面的细节特征。

分割出来的所有子图像都使用相同的图像编码器单独编码，以获取最大的信息度。

最后，把这些子图像的特征和全局图像的特征都输入到核心的大语言模型(LLM)中。

![](https://inews.gtimg.com/news_bt/OqCVOENl7gQs2HSjtzUpLLnMi9XFwrfHPIelyDa4CEvVAAA/1000)
靠着这种“用放大镜分别观察”的模式，最终FerryUI模型就能够更好地捕捉UI界面的细节信息。

解决第二个问题更简单，缺数据识别不了， 那就在训练阶段狂喂相关数据。

Ferry
UI收集了各种初级UI任务的训练数据，如图标识别、查找文本、组件列表等。这些任务数据训练模型精确定位和理解UI组件。同时它还收集了与AI交互相关的高级任务数据集，包括详细描述、感知/交互对话和功能推理，来增强模型和UI相关的推理能力。

经过了这样的UI强化训练，最终的结果就是，13B的FerryUI在完成初级和高级的UI相关对话后的能力，iPhone环境下在初级UI任务中超越了GPT4-V，在包含高级任务的全任务平均得分非常相近。
虽然在安卓环境下FerryUI表现略差，但是这对苹果来说有什么关系呢？

![](https://inews.gtimg.com/news_bt/OaVTX79QAf70bYShyoK9f26lTkMy63ejkmxAjnfbIuszYAA/1000)
经过了FerryUI的升级，Ferry模型可以完成简单的定位类任务(Referring
Tasks):识别UI的边框，图标和其中的文字内容。识别类任务(Grounding
Tasks):给定一个UI相关的查询，模型需要在界面上定位并标注出相关的元素。

![](https://inews.gtimg.com/news_bt/OX7vBR-9LXNYNCXuaR7Vq4vrSHnZV69pKPqsDGzkfZarIAA/1000)
_（简单UI任务一览）_

同时它也可以完成更复杂的详细描述UI构成的任务；根据UI与用户进行感知对话、交互对话，可以告诉用户相应位置具体的UI内容是什么，如何去和该UI进行交互的任务；以及根据UI元素推断这个软件功能的功能推理任务。

这就意味着FerryUI已经建立起了对于手机应用的功能，操作的相对完整的理解。而且是GPT4级别的理解。

如果仅仅停留在理解这个层面上，FerryUI的应用其实是有限的。比如视障用户可以用语言交互来了解UI的位置，或者整合到苹果自身的图形识别系统中增强识别能力。

**但这种理解如果结合上Agent的功能，让FerryUI模型可以去基于用户的自然语言交互操作手机，那一个AI Native的手机系统雏形就诞生了。**

AI Native 的手机，而不是AI 手机

在过去的一年里，如何将AI大模型应用到手机里已经成了不论是芯片厂商，还是手机制造商最重要的议题。端侧大模型，AI手机的概念层出不穷。然而时至今日，芯片厂商和手机厂商们展示的AI大模型能力都还仅仅停留在手机系统之外。

一种方式就是硬塞一个大模型进去，通过云端或本地算力驱动。其体验和Kimi助手，GPT
app没有什么本质区别，最多就是可以读取手机上的相应数据，应用相对方便一点。

![](https://inews.gtimg.com/news_bt/OBxXYZjsYxZ4I2utQi5kJa48yXVJDmKK4ykT6yeDEZCWMAA/1000)
另一种方式就是将AI能力赋能在其预装应用之中，转变成如魔法修图，短信回复自动生成这种完全无需大模型就能在一定程度上实现的功能。

这样的应用方式让AI手机这个概念显得不伦不类，更像是装了AI大模型应用的手机。

而真正能够应对来势汹汹的AI新硬件的，至少应该是一个适应AI新交互的完全的手机系统。

现在FerryUI的出现，使得这件事成为了可能。

一个14B以下的，可以直接在手机本地运行的大模型，可以让你用自然语言控制UI，进行相关操作。如果这项功能整合在Siri上，那Siri就可以成为一切App的新入口，只要一句话你就可以控制手机的一切功能，以及所有App的相关功能。这其实和Rabitt
R1所设想的一样。

而且这一次，你并不用牺牲屏幕本身了。在体验Humane 的AI
Pin和其他AI智能设备时，虽然它们确实可以通过自然语言完成几乎所有的交互，但他们没有屏幕。没有屏幕这对于生活在视频时代的人类来讲几乎是无法忍耐的。另外，缺乏声音之外的交互方式也使得它们在你对面有人的时候根本不好意思用。

但如果手机能做到这种交互，而且还有屏幕的话。我们为什么还会需要一个新的所谓AI智能设备去完成这一切呢？

因此，兜兜转转了一年，苹果应该是找到了AI
手机的真意。如果情况顺利，也许我们在两个月后的WWDC上就能看到原生AI的苹果手机系统了。而且很有可能是第一款Native AI 手机系统。

Google和苹果，一场新竞争正式开赛

之所以说可能，是因为苹果在系统上的老对头谷歌，其实也做了一样的路线判断。

在半个月前的3月19日，谷歌发表了一个新模型ScreenAI，它和FerryUI一样，都是直指 UI
理解的多模态模型。它的架构相对简单，基于Pali，包含两个组成部分，一个视觉变换器
(ViT），用来理解UI视觉；一个T5图文编码器，用于对应用户提问的文字和图像信息。

为解决UI问题，基本上谷歌的操作和苹果没什么差别，它把UI界面分割成5*7的小块去识别细节，并利用UI相关的训练集加强模型对UI元素的认知。

虽然没有像苹果一样和GPT4进行比较，但它也和自家的Gemini
Ultra在UI任务上进行了比对，也是相差无多。值得注意的是ScreenAI比苹果的Ferett更小，仅有不到5B。谷歌还尝试着用ScreenAI串联
Palm2完成高级UI任务，能力足以超过Geminni Ultra。

![](https://inews.gtimg.com/news_bt/OVxwRO1JGD91M5NGq7-oNKMer1ORrwWydTncv6DvIIlMsAA/1000)
所以，2024年春天，智能手机OS届的两大霸主，在AI手机这件事上殊途同归。强于AI的谷歌和强于系统的苹果走到了同样的起跑线上。

![](https://inews.gtimg.com/news_bt/O3gXCPux3CjKuFdIVrXUiNXtBblmAYGyTv2c9QdcesxHwAA/1000)
现在的问题，只剩谁跑得快了。

谷歌 I / O大会在5月14日，苹果的WWDC在6月。争分夺秒的战争已经开始了。

