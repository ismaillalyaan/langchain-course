from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    information = """Elon Musk

Article
Talk
Read
View source
View history

Tools
Appearance hide
Text

Small

Standard

Large
Width

Standard

Wide
Color (beta)

Automatic

Light

Dark
Page extended-confirmed-protected
From Wikipedia, the free encyclopedia
For other uses, see Elon Musk (disambiguation).
Elon Musk
FRS

Musk in 2022
Senior Advisor to the President
In office
January 20, 2025 – May 30, 2025
Serving with Massad Boulos
President	Donald Trump
Preceded by	Tom Perez
Personal details
Born	Elon Reeve Musk
June 28, 1971 (age 54)
Pretoria, South Africa
Citizenship	
South Africa
Canada
United States
Political party	Independent
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2016)​
Children	at least 14 (including Vivian Wilson)
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Education	University of Pennsylvania (BA, BS)
Occupation	
CEO and product architect of Tesla
Founder, CEO, and chief engineer of SpaceX
Founder and CEO of xAI
Founder of the Boring Company and X Corp.
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
President of the Musk Foundation
Awards	Full list
Signature	
Elon Musk's voice
Duration: 1 minute and 13 seconds.1:13
Elon Musk on his departure from the Department of Government Efficiency
Recorded May 30, 2025
	
This article is part of
a series about
Elon Musk
Personal
Companies
Politics
In books
vte
Elon Reeve Musk[a] (born June 28, 1971) is an international businessman and entrepreneur known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). Musk has been the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.

Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he had obtained Canadian citizenship at birth through his Canadian-born mother. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.

In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI) research, but later left, growing discontent with the organization's direction and their leadership in the AI boom in the 2020s led him to establish xAI. In 2022, he acquired the social network Twitter, implementing significant changes, and rebranding it as X in 2023. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017.

Musk was the largest donor in the 2024 U.S. presidential election, and is a supporter of global far-right figures, causes, and political parties. In early 2025, he served as senior advisor to United States president Donald Trump and as the de facto head of DOGE. After a public feud with Trump, Musk left the Trump administration and announced he was creating his own political party, the America Party.

Musk's political activities, views, and statements have made him a polarizing figure, especially following the COVID-19 pandemic. He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation and promoting conspiracy theories, and affirming antisemitic, racist, and transphobic comments. His acquisition of Twitter was controversial due to a subsequent increase in hate speech and the spread of misinformation on the service. His role in the second Trump administration attracted public backlash, particularly in response to DOGE.

Early life
See also: Musk family
Elon Reeve Musk was born on June 28, 1971, in Pretoria, South Africa's administrative capital.[1][2] He is of British and Pennsylvania Dutch ancestry.[3][4] His mother, Maye (née Haldeman), is a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[5][6][7] Musk therefore holds both South African and Canadian citizenship from birth.[8] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, emerald dealer, and property developer, who partly owned a rental lodge at Timbavati Private Nature Reserve.[9][10][11][12]

His maternal grandfather, Joshua N. Haldeman, who died in a plane crash when Elon was a toddler, was an American-born Canadian chiropractor, aviator and political activist in the Technocracy movement[13][14] who moved to South Africa in 1950.[15] Haldeman's anti-government, anti-democratic and conspiracist views, which included the promotion of far-right antisemitic conspiracy theories,[16][17] "fanatical" support of apartheid,[17] and according to Errol Musk, support of Nazism,[15] have been suggested as an influence on Elon.[18][19][20][21] During his childhood, Elon was told stories by his grandmother of Haldeman's travels and exploits, and Elon has suggested that all of Haldeman's descendants have his "desire for adventure, exploration – doing crazy things".[22]

Elon has a younger brother, Kimbal, a younger sister, Tosca, and four paternal half-siblings.[23][24][7][25] Musk was raised in the Anglican Church, in which he was baptized.[26][27] The Musk family was wealthy during Elon's youth.[12] Despite both Elon and Errol previously stating that Errol was a part owner of a Zambian emerald mine,[12] in 2023, Errol recounted that the deal he made was to receive "a portion of the emeralds produced at three small mines".[28][29] Errol was elected to the Pretoria City Council as a representative of the anti-apartheid Progressive Party and has said that his children shared their father's dislike of apartheid.[1]

After his parents divorced in 1979, Elon, aged around 9, chose to live with his father because Errol Musk had an Encyclopædia Britannica and a computer.[30][3][9] Elon later regretted his decision and became estranged from his father.[31] Elon has recounted trips to a wilderness school that he described as a "paramilitary Lord of the Flies" where "bullying was a virtue" and children were encouraged to fight over rations.[32] In one incident, after an altercation with a fellow pupil, Elon was thrown down concrete steps and beaten severely, leading to him being hospitalized for his injuries.[33] Elon described his father berating him after he was discharged from the hospital.[33] Errol denied berating Elon and claimed, "The [other] boy had just lost his father to suicide, and Elon had called him stupid. Elon had a tendency to call people stupid. How could I possibly blame that child?"[34]

Elon was an enthusiastic reader of books, and had attributed his success in part to having read The Lord of the Rings, the Foundation series, and The Hitchhiker's Guide to the Galaxy.[11][35] At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual.[36] At age twelve, Elon sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500.[37][38]

Education
An ornate school building
Musk graduated from Pretoria Boys High School in South Africa.
Musk attended Waterkloof House Preparatory School, Bryanston High School, and then Pretoria Boys High School, where he graduated.[39] Musk was a good but unexceptional student, earning a 61 in Afrikaans and a B on his senior math certification.[40] Musk applied for a Canadian passport through his Canadian-born mother to avoid South Africa's mandatory military service,[41][42] which would have forced him to participate in the apartheid regime,[1] as well as to ease his path to immigration to the United States.[43] While waiting for his application to be processed, he attended the University of Pretoria for five months.[44]

Musk arrived in Canada in June 1989, connected with a second cousin in Saskatchewan,[45][46] and worked odd jobs, including at a farm and a lumber mill.[47] In 1990, he entered Queen's University in Kingston, Ontario.[48][49] Two years later, he transferred to the University of Pennsylvania, where he studied until 1995.[50] Although Musk has said that he earned his degrees in 1995, the University of Pennsylvania did not award them until 1997 – a Bachelor of Arts in physics and a Bachelor of Science in economics from the university's Wharton School.[51][52][53][54][55] He reportedly hosted large, ticketed house parties to help pay for tuition, and wrote a business plan for an electronic book-scanning service similar to Google Books.[56]

In 1994, Musk held two internships in Silicon Valley: one at energy storage startup Pinnacle Research Institute, which investigated electrolytic supercapacitors for energy storage, and another at Palo Alto–based startup Rocket Science Games.[57][58] In 1995, he was accepted to a graduate program in materials science at Stanford University, but did not enroll.[53][51][59] Musk decided to join the Internet boom, applying for a job at Netscape, to which he reportedly never received a response.[60][41] The Washington Post reported that Musk lacked legal authorization to remain and work in the United States after failing to enroll at Stanford.[59] In response, Musk said he was allowed to work at that time and that his student visa transitioned to an H1-B. According to numerous former business associates and shareholders, Musk said he was on a student visa at the time.[61]

Business career
Main article: Business career of Elon Musk
Zip2
Main article: Zip2
External videos
video icon Musk speaks of his early business experience during a 2014 commencement speech at University of Southern California on YouTube
In 1995, Musk, his brother Kimbal, and Greg Kouri founded the web software company Zip2 with funds borrowed from Musk's father.[62][31] They housed the venture at a small rented office in Palo Alto.[63] The company developed and marketed an Internet city guide for the newspaper publishing industry, with maps, directions, and yellow pages.[64]

According to Musk, "The website was up during the day and I was coding it at night, seven days a week, all the time."[63] The Musk brothers obtained contracts with The New York Times and the Chicago Tribune,[65] and persuaded the board of directors to abandon plans for a merger with CitySearch.[66] Musk's attempts to become CEO were thwarted by the board.[67] Compaq acquired Zip2 for $307 million in cash in February 1999,[68][69] and Musk received $22 million for his 7-percent share.[70]

X.com and PayPal
Main articles: X.com (bank), PayPal, and PayPal Mafia
In 1999, Musk co-founded X.com, an online financial services and e-mail payment company.[71] The startup was one of the first federally insured online banks, and, in its initial months of operation, over 200,000 customers joined the service.[72] The company's investors regarded Musk as inexperienced and replaced him with Intuit CEO Bill Harris by the end of the year.[73] The following year, X.com merged with online bank Confinity to avoid competition.[63][73][74] Founded by Max Levchin and Peter Thiel,[75] Confinity had its own money-transfer service, PayPal, which was more popular than X.com's service.[76]

Within the merged company, Musk returned as CEO. Musk's preference for Microsoft software over Unix created a rift in the company and caused Thiel to resign.[77] Due to resulting technological issues and lack of a cohesive business model, the board ousted Musk and replaced him with Thiel in 2000.[78][b] Under Thiel, the company focused on the PayPal service and was renamed PayPal in 2001.[80][81] In 2002, PayPal was acquired by eBay for $1.5 billion in stock, of which Musk—the largest shareholder with 11.72% of shares—received $175.8 million.[82][83] In 2017, Musk purchased the domain X.com from PayPal for an undisclosed amount, stating that it had sentimental value.[84][85]

SpaceX
Main article: SpaceX

Musk explains Starship capabilities to leaders of North American Aerospace Defense Command, U.S. Northern Command, and Air Force Space Command in 2019.
In 2001, Musk became involved with the nonprofit Mars Society and discussed funding plans to place a growth-chamber for plants on Mars.[86] Seeking a way to launch the greenhouse payloads into space, Musk made two unsuccessful trips to Moscow to purchase intercontinental ballistic missiles (ICBMs) from Russian companies NPO Lavochkin and Kosmotras. Musk instead decided to start a company to build affordable rockets.[87] With $100 million of his early fortune,[88] Musk founded SpaceX in May 2002 and became the company's CEO and Chief Engineer.[89][90]

SpaceX attempted its first launch of the Falcon 1 rocket in 2006.[91] Although the rocket failed to reach Earth orbit, it was awarded a Commercial Orbital Transportation Services program contract from NASA, then led by Mike Griffin.[92][93] After two more failed attempts that nearly caused Musk to go bankrupt,[91] SpaceX succeeded in launching the Falcon 1 into orbit in 2008.[94] Later that year, SpaceX received a $1.6 billion NASA contract for Falcon 9-launched Dragon spacecraft flights to the International Space Station (ISS), replacing the Space Shuttle after its 2011 retirement.[95] In 2012, the Dragon vehicle docked with the ISS, a first for a commercial spacecraft.[96]

Working towards its goal of reusable rockets, in 2015 SpaceX successfully landed the first stage of a Falcon 9 on a land platform.[97] Later landings were achieved on autonomous spaceport drone ships, an ocean-based recovery platform.[98] In 2018, SpaceX launched the Falcon Heavy; the inaugural mission carried Musk's personal Tesla Roadster as a dummy payload.[99][100] Since 2019,[101] SpaceX has been developing Starship, a reusable, super heavy-lift launch vehicle intended to replace the Falcon 9 and Falcon Heavy.[102] In 2020, SpaceX launched its first crewed flight, the Demo-2, becoming the first private company to place astronauts into orbit and dock a crewed spacecraft with the ISS.[103] In 2024, NASA awarded SpaceX an $843 million contract to deorbit the ISS at the end of its lifespan.[104]

Starlink
Main article: Starlink
See also: Starlink in the Russo-Ukrainian War

50 Starlink satellites shortly before deployment to low Earth orbit, 2019
In 2015, SpaceX began development of the Starlink constellation of low Earth orbit satellites to provide satellite Internet access.[105] After the launch of prototype satellites in 2018, the first large constellation was deployed in May 2019.[106] As of May 2025, over 7,600 Starlink satellites are operational,[107] comprising 65% of all operational Earth satellites.[108] The total cost of the decade-long project to design, build, and deploy the constellation was estimated by SpaceX in 2020 to be $10 billion.[109][c]

During the Russian invasion of Ukraine, Musk provided free Starlink service to Ukraine, permitting Internet access and communication at a yearly cost to SpaceX of $400 million.[112][113][114][115][116] However, Musk refused to block Russian state media on Starlink.[117][118] In 2023, Musk denied Ukraine's request to activate Starlink over Crimea to aid an attack against the Russian navy, citing fears of a nuclear response.[119][120][121]

Tesla
Main article: Tesla, Inc.
Musks stands, arms crossed and grinning, before a Tesla Model S
Musk next to a Tesla Model S, 2011
Tesla, Inc., originally Tesla Motors, was incorporated in July 2003 by Martin Eberhard and Marc Tarpenning. Both men played active roles in the company's early development prior to Musk's involvement.[122] Musk led the Series A round of investment in February 2004; he invested $6.35 million, became the majority shareholder, and joined Tesla's board of directors as chairman.[123][124] Musk took an active role within the company and oversaw Roadster product design, but was not deeply involved in day-to-day business operations.[125] Following a series of escalating conflicts in 2007 and the 2008 financial crisis, Eberhard was ousted from the firm.[126][page needed][127] Musk assumed leadership of the company as CEO and product architect in 2008.[128] A 2009 lawsuit settlement with Eberhard designated Musk as a Tesla co-founder, along with Tarpenning and two others.[129][130]

Tesla began delivery of the Roadster, an electric sports car, in 2008. With sales of about 2,500 vehicles, it was the first mass production all-electric car to use lithium-ion battery cells.[131] Under Musk, Tesla has since launched several well-selling electric vehicles, including the four-door sedan Model S (2012), the crossover Model X (2015), the mass-market sedan Model 3 (2017), the crossover Model Y (2020), and the pickup truck Cybertruck (2023).[132][133][134][135][136]

In May 2020 Musk resigned as chairman of the board as part of the settlement of a lawsuit from the SEC over him tweeting that funding had been "secured" for potentially taking Tesla private.[137][138]

The company has also constructed multiple lithium-ion battery and electric vehicle factories, called Gigafactories.[139] Since its initial public offering in 2010,[140] Tesla stock has risen significantly; it became the most valuable carmaker in summer 2020,[141][142] and it entered the S&P 500 later that year.[143][144] In October 2021, it reached a market capitalization of $1 trillion, the sixth company in U.S. history to do so.[145]

SolarCity and Tesla Energy
Main articles: SolarCity and Tesla Energy
Two green vans sporting the SolarCity logo
SolarCity solar-panel installation vans in 2009
Musk provided the initial concept and financial capital for SolarCity, which his cousins Lyndon and Peter Rive founded in 2006.[146] By 2013, SolarCity was the second largest provider of solar power systems in the United States.[147] In 2014, Musk promoted the idea of SolarCity building an advanced production facility in Buffalo, New York, triple the size of the largest solar plant in the United States.[148] Construction of the factory started in 2014 and was completed in 2017. It operated as a joint venture with Panasonic until early 2020.[149][150]

Tesla acquired SolarCity for $2 billion in 2016 and merged it with its battery unit to create Tesla Energy. The deal's announcement resulted in a more than 10% drop in Tesla's stock price; at the time, SolarCity was facing liquidity issues.[151] Multiple shareholder groups filed a lawsuit against Musk and Tesla's directors, stating that the purchase of SolarCity was done solely to benefit Musk and came at the expense of Tesla and its shareholders.[152][153] Tesla directors settled the lawsuit in January 2020, leaving Musk the sole remaining defendant.[154][155] Two years later, the court ruled in Musk's favor.[151]

Neuralink
Main article: Neuralink
Musk standing next to bulky medical equipment on a stage
Musk discussing a Neuralink device during a live demonstration in 2020
In 2016, Musk co-founded Neuralink, a neurotechnology startup, with an investment of $100 million.[156][157] Neuralink aims to integrate the human brain with artificial intelligence (AI) by creating devices that are embedded in the brain. Such technology could enhance memory or allow the devices to communicate with software.[157][158] The company also hopes to develop devices to treat neurological conditions like spinal cord injuries.[159] In 2022, Neuralink announced that clinical trials would begin by the end of the year.[160] In September 2023, the Food and Drug Administration approved Neuralink to initiate six-year human trials.[161]

Neuralink has conducted animal testing on macaques at the University of California, Davis. In 2021, the company released a video in which a macaque played the video game Pong via a Neuralink implant. The company's animal trials—which have caused the deaths of some monkeys—have led to claims of animal cruelty. The Physicians Committee for Responsible Medicine has alleged that Neuralink violated the Animal Welfare Act.[162] Employees have complained that pressure from Musk to accelerate development has led to botched experiments and unnecessary animal deaths. In 2022, a federal probe was launched into possible animal welfare violations by Neuralink.[163]

The Boring Company
Main article: The Boring Company
Musk speaks to a crowd of journalists. Behind him is a lighted tunnel.
Musk during the 2018 inauguration of the Boring test tunnel in Hawthorne, California
In 2017, Musk founded the Boring Company to construct tunnels; he also revealed plans for specialized, underground, high-occupancy vehicles that could travel up to 150 miles per hour (240 km/h) and thus circumvent above-ground traffic in major cities.[164][165] Early in 2017, the company began discussions with regulatory bodies and initiated construction of a 30-foot (9.1 m) wide, 50-foot (15 m) long, and 15-foot (4.6 m) deep "test trench" on the premises of SpaceX's offices, as that required no permits.[166]

The Los Angeles tunnel, less than two miles (3.2 km) in length, debuted to journalists in 2018. It used Tesla Model Xs and was reported to be a rough ride while traveling at suboptimal speeds.[167] Two tunnel projects announced in 2018, in Chicago and West Los Angeles, have been canceled.[168][169] A tunnel beneath the Las Vegas Convention Center was completed in early 2021.[170] Local officials have approved further expansions of the tunnel system.[171]

X Corp.
Main articles: Acquisition of Twitter by Elon Musk and Twitter under Elon Musk
Avatar of Elon Musk
Elon Musk 
@elonmusk
I made an offer
https://sec.gov/Archives/edgar...

April 14, 2022[172]
In early 2017, Musk expressed interest in buying Twitter and had questioned the platform's commitment to freedom of speech.[173][174][175] By 2022, Musk had reached 9.2% stake in the company,[176] making him the largest shareholder.[177][d] Musk later agreed to a deal that would appoint him to Twitter's board of directors and prohibit him from acquiring more than 14.9% of the company.[179][180] Days later, Musk made a $43 billion offer to buy Twitter.[177][181] By the end of April Musk had successfully concluded his bid for approximately $44 billion.[182] This included approximately $12.5 billion in loans and $21 billion in equity financing.[183][184] Having backtracked on his initial decision,[185] Musk bought the company on October 27, 2022.[186]

Immediately after the acquisition, Musk fired several top Twitter executives including CEO Parag Agrawal;[186][187] Musk became the CEO instead.[188] Under Elon Musk, Twitter instituted monthly subscriptions for a "blue check",[189][190][191] and laid off a significant portion of the company's staff.[192][193] Musk lessened content moderation and hate speech also increased on the platform after his takeover.[194][195][196][197] In late 2022, Musk released internal documents relating to Twitter's moderation of Hunter Biden's laptop controversy in the lead-up to the 2020 presidential election.[198] Musk also promised to step down as CEO after a Twitter poll,[199][200] and five months later, Musk stepped down as CEO and transitioned his role to executive chairman and chief technology officer (CTO).[201]

Despite Musk stepping down as CEO, X continues to struggle with challenges such as viral misinformation,[202] hate speech, and antisemitism controversies.[203][204] Musk has been accused of trying to silence some of his critics such as Twitch streamer Asmongold, who criticized him during one of his streams.[205] Musk has been accused of removing their accounts' blue checkmarks, which hinders visibility and is considered a form of shadow banning,[206][207] or suspending their accounts without justification.[208]

Other activities
In 2025, Axios reported that Musk had previously participated in Dialog, an invite-only forum co-founded by Peter Thiel and Auren Hoffman.[209]

Hyperloop
Main articles: Hyperloop and Hyperloop pod competition
A long white tube about 10 feet in diameter
A tube part of the 2017 Hyperloop pod competition, sponsored by SpaceX
In August 2013, Musk announced plans for a version of a vactrain, and assigned engineers from SpaceX and Tesla to design a transport system between Greater Los Angeles and the San Francisco Bay Area, at an estimated cost of $6 billion.[210][211] Later that year, Musk unveiled the concept, dubbed the Hyperloop,[212] intended to make travel cheaper than any other mode of transport for such long distances.[213]

OpenAI and xAI
Main articles: OpenAI and xAI (company)
In December 2015, Musk co-founded OpenAI, a not-for-profit artificial intelligence (AI) research company aiming to develop artificial general intelligence, intended to be safe and beneficial to humanity.[214] Musk pledged $1 billion of funding to the company,[215] but only donated $50 million.[216] In 2018, Musk left the OpenAI board.[217] Since 2018, OpenAI has made significant advances in machine learning.[218] In July 2023, Musk launched the artificial intelligence company xAI, which aims to develop a generative AI program that competes with existing offerings like OpenAI's ChatGPT. Musk obtained funding from investors in SpaceX and Tesla,[219] and xAI hired engineers from Google and OpenAI.[220]

Private jet
Main articles: ElonJet and 2022 Twitter suspensions
Avatar of Elon Musk
Elon Musk
@elonmusk
Same doxxing rules apply to "journalists" as to everyone else

December 16, 2022[221]
Musk uses a private jet owned by Falcon Landing LLC, a SpaceX-linked company, and acquired a second jet in August 2020.[222][223] His heavy use of the jets and the consequent fossil fuel usage have received criticism.[222][224] Musk's flight usage is tracked on social media through ElonJet.[225][226][227] In December 2022, Musk banned the ElonJet account on Twitter, and made temporary bans on the accounts of journalists that posted stories regarding the incident, including Donie O'Sullivan, Keith Olbermann, and journalists from The New York Times, The Washington Post, CNN, and The Intercept.[228]

Politics
Main article: Political activities of Elon Musk
See also: Protests against Elon Musk

Musk with then-president-elect Donald Trump in November 2024
Musk is an outlier among business leaders who typically avoid partisan political advocacy.[229][230][231] Musk was a registered independent voter when he lived in California.[232] Historically, he has donated to both Democrats and Republicans,[233] many of whom serve in states in which he has a vested interest.[234] Since 2022, his political contributions have mostly supported Republicans, with his first vote for a Republican going to Mayra Flores in the 2022 Texas's 34th congressional district special election.[235][236] In 2024, he started supporting international far-right political parties, activists, and causes,[237] and has shared far-right misinformation[238][239][240] and numerous conspiracy theories.[241][242] Since 2024, his views have been generally described as right-wing.[243]

Musk supported Barack Obama in 2008 and 2012,[244] Hillary Clinton in 2016, Joe Biden in 2020,[245] and Donald Trump in 2024.[246] In the 2020 Democratic Party presidential primaries, Musk endorsed candidate Andrew Yang and expressed support for Yang's proposed universal basic income,[247] and endorsed Kanye West's 2020 presidential campaign.[248] In 2021, Musk publicly expressed opposition to the Build Back Better Act, a $3.5 trillion legislative package endorsed by Joe Biden that ultimately failed to pass due to unanimous opposition from congressional Republicans and several Democrats.[249]

In 2022, Musk said he would start supporting Republican Party candidates,[250] and gave over $50 million to Citizens for Sanity, a conservative political action committee.[251] In 2023, he supported Republican Ron DeSantis for the 2024 U.S. presidential election, giving $10 million to his campaign,[251] and hosted DeSantis's campaign announcement on a Twitter Spaces event.[252][253][254] From June 2023 to January 2024, Musk hosted a bipartisan set of X Spaces with Republican and Democratic candidates, including Robert F. Kennedy Jr.,[255] Vivek Ramaswamy,[256] and Dean Phillips.[257]


Musk at a 2024 gathering with Trump and other political leaders
By early 2024, Musk had become a vocal and financial supporter of Donald Trump.[258] In July 2024, minutes after the attempted assassination of Donald Trump, Musk endorsed him for president saying; "I fully endorse President Trump and hope for his rapid recovery."[259][260] During the presidential campaign, Musk joined Trump on stage at a campaign rally,[261] and during the campaign promoted conspiracy theories and falsehoods about Democrats, election fraud[262] and immigration, in support of Trump.[263][264] Musk was the largest individual donor of the 2024 election.[265] In 2025, Musk contributed $19 million to the Wisconsin Supreme Court race, hoping to influence the state's future redistricting efforts and its regulations governing car manufacturers and dealers.[266][267]

Musk's international political actions and comments have come under increasing scrutiny and criticism, especially from the governments and leaders of France, Germany, Norway, Spain and the United Kingdom, particularly due to his position in the U.S. government as well as ownership of X.[268][269][270] An NBC News analysis found he had boosted far-right political movements to cut immigration and curtail regulation of business in at least 18 countries on six continents since 2023.[271]

Salute at Trump's second inauguration
Main article: Elon Musk salute controversy

Musk giving a gesture at the second inauguration of Donald Trump before saying "My heart goes out to you. It is thanks to you that the future of civilization is assured."[272][273]
During his speech after the second inauguration of Donald Trump, Musk twice made a gesture interpreted by many as a Nazi or a fascist Roman salute.[e] He thumped his right hand over his heart, fingers spread wide, and then extended his right arm out, emphatically, at an upward angle, palm down and fingers together. He then repeated the gesture to the crowd behind him. As he finished the gestures, he said to the crowd, "My heart goes out to you. It is thanks to you that the future of civilization is assured."[272][273][275]

It was widely condemned as an intentional Nazi salute in Germany,[276][277][278] where making such gestures is illegal.[279] The Anti-Defamation League said it was not a Nazi salute,[280] but other Jewish organizations disagreed and condemned the salute.[281][282][283][284] American public opinion was divided on partisan lines as to whether it was a fascist salute.[285] Musk dismissed the accusations of Nazi sympathies, deriding them as "dirty tricks" and a "tired" attack.[286][287] Neo-Nazi and white supremacist groups celebrated it as a Nazi salute.[288][280] Multiple European political parties demanded that Musk be banned from entering their countries.[289][290]

Department of Government Efficiency
Main article: Department of Government Efficiency

Elon Musk wielding a chainsaw at the Conservative Political Action Conference (CPAC) in 2025, imitating a publicity stunt used by Javier Milei symbolic of efficiency, federal mass layoffs and tax cutting
The concept of DOGE emerged in a discussion between Musk and Donald Trump, and in August 2024, Trump committed to giving Musk an advisory role, with Musk accepting the offer.[291] In November and December 2024, Musk suggested that the organization could help to cut the U.S. federal budget, consolidate the number of federal agencies,[292][293] and eliminate the Consumer Financial Protection Bureau,[294][295] and that its final stage would be "deleting itself".[296]

In January 2025, the organization was created by executive order, and Musk was designated a "special government employee".[297][298] Musk is leading the organization and is a senior advisor to the president,[299] although his official role is not clear.[300] In sworn statement during a lawsuit, the director of the White House Office of Administration stated that Musk "is not an employee of the U.S. DOGE Service or U.S. DOGE Service Temporary Organization", "is not the U.S. DOGE Service administrator", and has "no actual or formal authority to make government decisions himself".[301][302] Trump said two days later that he had put Musk in charge of DOGE.[303] A federal judge has ruled that Musk acts as the de facto leader of DOGE.[304]

Elon Musk participating in a press conference with Donald Trump shortly before his departure from DOGE
Musk's role in the second Trump administration, particularly in response to DOGE, has attracted public backlash. He was criticized for his treatment of federal government employees,[305][306][307] including his influence over the mass layoffs of the federal workforce.[308][309][310] He has prioritized secrecy within the organization[311] and has accused others of violating privacy laws.[297] A Senate report alleged that Musk could avoid up to $2 billion in legal liability as a result of DOGE's actions[312] In May 2025, Bill Gates accused Musk of "killing the world's poorest children" through his cuts to USAID,[313] which modeling by Boston University estimated had resulted in 300,000 deaths by this time, most of them of children.[314][315]

Musk announced on May 28, 2025, that he would depart from the Trump administration as planned when the special government employee's 130 day deadline expired,[316] with a White House official confirming that Musk's offboarding from the Trump administration was already underway.[317] His departure was officially confirmed during a joint Oval Office press conference with Trump on May 30, 2025.[318]

Feud with Donald Trump
Main article: Trump–Musk feud
Avatar of Elon Musk
Elon Musk
@elonmusk
Time to drop the really big bomb:

@realDonaldTrump is in the Epstein files. That is the real reason they have not been made public.

Have a nice day, DJT!

June 5, 2025[319]
After leaving office, Musk criticized the Trump administration's Big Beautiful Bill, calling it a "disgusting abomination" due to its provisions increasing the deficit.[320] A feud began between Musk and Trump, with its most notable event being Musk alleging Trump had ties to sex offender Jeffrey Epstein on X (formerly Twitter) on June 5, 2025.[321][322] Trump responded on Truth Social stating that Musk went "CRAZY" after the "EV Mandate" was purportedly taken away and threatened to cut Musk's government contracts.[323][324] Musk then called for a third Trump impeachment.[325] The next day, Trump stated that he did not wish to reconcile with Musk, and added that Musk would face "very serious consequences" if he funds Democratic candidates.[326] On June 11, Musk publicly apologized for the tweets against Trump, saying they "went too far."[327]

Views
Main article: Views of Elon Musk
Avatar of Elon Musk
Elon Musk
@elonmusk
My commitment to free speech extends even to not banning the account following my plane, even though that is a direct personal safety risk

November 6, 2022[328]
Rejecting the conservative label,[329] Musk has described himself as a political moderate, even as his views have become more right-wing over time.[330] His views have been characterized as libertarian and far-right,[331][332] and after his involvement in European politics, they have received criticism from world leaders such as Emmanuel Macron and Olaf Scholz.[333][334][335][336]

Within the context of American politics, Musk supported Democratic candidates up until 2022, at which point he voted for a Republican for the first time.[244][250][246] He has stated support for universal basic income,[337] gun rights,[338] freedom of speech,[339] a tax on carbon emissions,[340] and H-1B visas.[341] Musk has expressed concern about issues such as artificial intelligence (AI)[342] and climate change,[343] and has been a critic of wealth tax,[344] short-selling,[345] and government subsidies.[346] An immigrant himself, Musk has been accused of being anti-immigration, and regularly blames immigration policies for illegal immigration.[347] He is also a pronatalist who believes population decline is the biggest threat to civilization,[348] and believes in the principles of Christianity.[349][350] Musk has long been an advocate for space colonization, especially the colonization of Mars. He has repeatedly pushed for humanity colonizing Mars, in order to become an interplanetary species and lower the risks of human extinction.[351]

Musk has promoted conspiracy theories and made controversial statements that have led to accusations of racism, sexism, antisemitism,[352][353] transphobia,[354] disseminating disinformation, and support of white pride.[355][356] While describing himself as a "pro-Semite",[357] his comments regarding George Soros and Jewish communities have been condemned by the Anti-Defamation League and the White House.[358] Musk was criticized during the COVID-19 pandemic for making unfounded epidemiological claims,[359] defied COVID-19 lockdowns restrictions,[360] and supported the Canada convoy protest against vaccine mandates.[361][362] He has amplified false claims of white genocide in South Africa.[363]

International relations
Main article: International relations of Elon Musk

Musk with Israeli president Isaac Herzog, November 2023
Musk has been critical of Israel's actions in the Gaza Strip during the Gaza war,[364] praised China's economic and climate goals,[365][366] suggested that Taiwan and China should resolve cross-strait relations,[367][368] and was described as having a close relationship with the Chinese government.[365][366]

In Europe, Musk expressed support for Ukraine in 2022 during the Russian invasion, recommended referendums and peace deals on the annexed Russia-occupied territories,[369][370] and supported the far-right Alternative for Germany in Germany in 2024.[371] Regarding British politics, Musk blamed the 2024 UK riots on mass migration and open borders,[372][373] criticized Prime Minister Keir Starmer for what he described as a "two-tier" policing system,[374][375][373] and was subsequently attacked as being responsible for spreading misinformation and amplifying the far-right.[376] He has also voiced his support for far-right activist Tommy Robinson and pledged electoral support for Reform UK.[377][378]

Legal affairs
Main article: Legal affairs of Elon Musk
Further information: List of lawsuits involving Tesla, Inc. and Criticism of Tesla, Inc.
In 2018, Musk was sued by the U.S. Securities and Exchange Commission (SEC) for a tweet stating that funding had been secured for potentially taking Tesla private.[137][f] The securities fraud lawsuit characterized the tweet as false, misleading, and damaging to investors, and sought to bar Musk from serving as CEO of publicly traded companies.[137][382][383] Two days later, Musk settled with the SEC, without admitting or denying the SEC's allegations. As a result, Musk and Tesla were fined $20 million each, and Musk was forced to step down for three years as Tesla chairman but was able to remain as CEO.[138] Shareholders filed a lawsuit over the tweet,[384] and in February 2023, a jury found Musk and Tesla not liable.[385] Musk has stated in interviews that he does not regret posting the tweet that triggered the SEC investigation.[386][387]

In 2019, Musk stated in a tweet that Tesla would build half a million cars that year.[388] The SEC reacted by asking a court to hold him in contempt for violating the terms of the 2018 settlement agreement. A joint agreement between Musk and the SEC eventually clarified the previous agreement details,[389] including a list of topics about which Musk needed preclearance.[390] In 2020, a judge blocked a lawsuit that claimed a tweet by Musk regarding Tesla stock price ("too high imo") violated the agreement.[391][392] Freedom of Information Act (FOIA)-released records showed that the SEC concluded Musk had subsequently violated the agreement twice by tweeting regarding "Tesla's solar roof production volumes and its stock price".[393]

In October 2023, the SEC sued Musk over his refusal to testify a third time in an investigation into whether he violated federal law by purchasing Twitter stock in 2022.[394][395][396] In February 2024, Judge Laurel Beeler ruled that Musk must testify again.[397] In January 2025, the SEC filed a lawsuit against Musk for securities violations related to his purchase of Twitter.[398] In January 2024, Delaware judge Kathaleen McCormick ruled in a 2018 lawsuit that Musk's $55 billion pay package from Tesla be rescinded.[399] McCormick called the compensation granted by the company's board "an unfathomable sum" that was unfair to shareholders.[400]

Personal life
Musk became a U.S. citizen in 2002.[50] From the early 2000s until late 2020, Musk resided in California, where both Tesla and SpaceX were founded.[401] He then relocated to Cameron County, Texas,[402][403] saying that California had become "complacent" about its economic success.[401][404][405]

While hosting Saturday Night Live in 2021, Musk stated that he has Asperger syndrome (now merged with autism spectrum disorder).[406][407] When asked about his experience growing up with Asperger's syndrome in a TED2022 conference in Vancouver, Musk stated that "the social cues were not intuitive ... I would just tend to take things very literally ... but then that turned out to be wrong — [people were not] simply saying exactly what they mean, there's all sorts of other things that are meant, and [it] took me a while to figure that out."[408] Musk suffers from back pain and has undergone several spine-related surgeries, including a disc replacement.[409][410] In 2000, he contracted a severe case of malaria while on vacation in South Africa.[411]

Musk has stated he uses doctor-prescribed ketamine for occasional depression and that he doses "a small amount once every other week or something like that";[412] since January 2024, some media outlets have reported that he takes ketamine, marijuana, LSD, ecstasy, mushrooms, cocaine and other drugs. Musk at first refused to comment on his alleged drug use, before responding that he had not tested positive for drugs, and that if drugs somehow improved his productivity, "I would definitely take them!".[413] The New York Times' investigations revealed Musk's overuse of ketamine and numerous other drugs, as well as strained family relationships and concerns from close associates who have become troubled by his public behavior as he became more involved in political activities and government work.[414] According to The Washington Post, President Trump described Musk as "a big-time drug addict".[415]

Through his own label Emo G Records, Musk released a rap track, "RIP Harambe", on SoundCloud in March 2019.[416][417][418] The following year, he released an EDM track, "Don't Doubt Ur Vibe", featuring his own lyrics and vocals.[419]

Musk plays video games, which he stated has a "'restoring effect' that helps his 'mental calibration'".[420] Some games he plays include Quake, Diablo IV, Elden Ring, and Polytopia.[421][422] Musk once claimed to be one of the world's top video game players but has since admitted to "account boosting", or cheating by hiring outside services to achieve top player rankings.[423][424][425] Musk has justified the boosting by claiming that all top accounts do it so he has to as well to remain competitive.[426][425][427] In 2024 and 2025, Musk criticized the video game Assassin's Creed Shadows and its creator Ubisoft for "woke" content.[428] Musk posted to X that "DEI kills art" and specified the inclusion of the historical figure Yasuke in the Assassin's Creed game as offensive; he also called the game "terrible". Ubisoft responded by saying that Musk's comments were "just feeding hatred" and that they were focused on producing a game not pushing politics.[429][430]

Relationships and children
Further information: Musk family

Musk with his son, X Æ A-Xii, in the Oval Office, February 11, 2025
Musk has fathered at least 14 children, one of whom died as an infant.[431] The Wall Street Journal reported in 2025 that sources close to Musk suggest that the "true number of Musk's children is much higher than publicly known".[432] He had six children with his first wife, Canadian author Justine Wilson, who he met while attending Queen's University in Ontario, Canada; they married in 2000.[433] In 2002, their first child Nevada Musk died of sudden infant death syndrome at the age of 10 weeks.[434] After his death, the couple used in vitro fertilization (IVF) to continue their family;[435] they had twins in 2004, followed by triplets in 2006.[435] The couple divorced in 2008 and have shared custody of their children.[436][437] The elder twin he had with Wilson came out as a trans woman and, in 2022, officially changed her name to Vivian Jenna Wilson,[438] adopting her mother's surname because she no longer wished to be associated with Musk.[438]

Musk began dating English actress Talulah Riley in 2008.[439] They married two years later at Dornoch Cathedral in Scotland.[440][441] In 2012, the couple divorced, then remarried the following year.[442] After briefly filing for divorce in 2014,[442] Musk finalized a second divorce from Riley in 2016.[443] Musk then dated the American actress Amber Heard for several months in 2017;[444] he had reportedly been "pursuing" her since 2012.[445]

In 2018, Musk and Canadian musician Grimes confirmed they were dating.[446] Grimes and Musk have three children, born in 2020, 2021, and 2022.[447][448][449][450] Musk and Grimes originally gave their eldest child the name "X Æ A-12", which would have violated California regulations as it contained characters that are not in the modern English alphabet;[451][452] the names registered on the birth certificate are "X" as a first name, "Æ A-Xii" as a middle name, and "Musk" as a last name.[453][454] They received criticism for choosing a name perceived to be impractical and difficult to pronounce;[455] Musk has said the intended pronunciation is "X Ash A Twelve".[454] Their second child was born via surrogacy.[456] Despite the pregnancy, Musk confirmed reports that the couple were "semi-separated" in September 2021; in an interview with Time in December 2021, he said he was single.[457][458] In October 2023, Grimes sued Musk over parental rights and custody of X Æ A-Xii.[459][460][461] Elon Musk has taken X Æ A-Xii to multiple official events in Washington, D.C. during Trump's second term in office.[462]

Also in July 2022, The Wall Street Journal reported that Musk allegedly had an affair with Nicole Shanahan, the wife of Google co-founder Sergey Brin, in 2021, leading to their divorce the following year.[463] Musk denied the report.[464] Musk also had a relationship with Australian actress Natasha Bassett, who has been described as "an occasional girlfriend".[465] In October 2024, The New York Times reported Musk bought a Texas compound for his children and their mothers,[466] though Musk denied having done so.[467]

Musk also has four children with Shivon Zilis, director of operations and special projects at Neuralink: twins born via IVF in 2021, a child born in 2024 via surrogacy and a child born in 2025.[468][469][470][471][472][473] Musk allegedly had a child with author Ashley St. Clair in 2024.[432][474]

On February 14, 2025, Ashley St. Clair, an influencer and author, posted on X claiming to have given birth to Musk's son Romulus five months earlier, which media outlets reported as Musk's supposed thirteenth child.[475][476] On February 22, 2025, it was reported that St Clair had filed for sole custody of her five-month-old son and for Musk to be recognised as the child's father.[477][478] On March 31, 2025, Musk wrote that, while he was unsure if he was the father of St. Clair's child, he had paid St. Clair $2.5 million and would continue paying her $500,000 per year.[479][480][481][482][483] Later reporting from the Wall Street Journal indicated that $1 million of these payments to St. Clair was structured as a loan.[432]

Wealth
These paragraphs are an excerpt from Wealth of Elon Musk.[edit]
Elon Musk is the wealthiest person in the world, with an estimated net worth of US$384 billion as of September 2025, according to the Bloomberg Billionaires Index,[484] and $415.6 billion according to Forbes,[485] primarily from his ownership stakes in Tesla and SpaceX.

Having been first listed on the Forbes Billionaires List in 2012,[486] around 75% of Musk's wealth was derived from Tesla stock in November 2020.[487] Describing himself as "cash poor",[488][489] he became the first person in the world to have a net worth above $300 billion a year later. By December 2024, he became the first person to reach a net worth of $400 billion.[490] in early 2025, Musk's net worth was briefly over $487 billion according to Forbes.[491]
Musk Foundation
Main article: Musk Foundation
Musk is president of the Musk Foundation he founded in 2001,[492][493] whose stated purpose is to provide solar-power energy systems in disaster areas, with an interest in human space exploration, pediatrics, renewable energy, and "safe artificial intelligence".[494] From 2002 to 2018, the foundation donated nearly half of its $25 million directly to Musk's OpenAI.[495][496] The foundation's assets reached $9.4 billion by the end of 2021, but it only dispensed $160 million to charities that year.[497]

The Musk Foundation has been criticized for its "self-serving"[497] donations to efforts close to Musk's family and companies,[498] as well as its low payout ratio.[497][499] In 2021, after Musk challenged World Food Programme director David Beasley to draft a plan to use money of Musk's that Beasley said could contribute to ending world hunger,[500][501] Musk instead donated the $6 billion in question to his own foundation even after Beasley's plan showed that the money could feed 42 million people for a year.[502][497][503]

Public image
Main article: Public image of Elon Musk
Although his ventures have been highly influential within their separate industries starting in the 2000s, Musk only became a public figure in the early 2010s. He has been described as an eccentric who makes spontaneous and impactful decisions, while also often making controversial statements, contrary to other billionaires who prefer reclusiveness to protect their businesses. Musk's actions and his expressed views have made him a polarizing figure.[504] Biographer Ashlee Vance described people's opinions of Musk as polarized due to his "part philosopher, part troll" persona on Twitter.[505]

Musk has been described as an American oligarch due to his extensive influence over public discourse, social media, industry, politics, and government policy.[506] After Trump's re-election, Musk's influence and actions during the transition period and the second presidency of Donald Trump led some to call him "President Musk", the "actual president-elect", "shadow president" or "co-president".[507][508]

Accolades
Main article: List of awards and honors received by Elon Musk
Musk wearing a medal
Musk receiving the Order of Defence Merit from the Brazilian Armed Forces in 2022[509]
Awards for his contributions to the development of the Falcon rockets include the American Institute of Aeronautics and Astronautics George Low Transportation Award in 2008,[510] the Fédération Aéronautique Internationale Gold Space Medal in 2010,[511] and the Royal Aeronautical Society Gold Medal in 2012.[512] In 2015, he received an honorary doctorate in engineering and technology from Yale University[513] and an Institute of Electrical and Electronics Engineers Honorary Membership.[514] Musk was elected a Fellow of the Royal Society (FRS) in 2018.[515][g] In 2022, Musk was elected to the National Academy of Engineering.[517]

Time has listed Musk as one of the most influential people in the world in 2010,[518] 2013,[519] 2018,[520] and 2021.[521] Musk was selected as Time's "Person of the Year" for 2021. Then Time editor-in-chief Edward Felsenthal wrote that, "Person of the Year is a marker of influence, and few individuals have had more influence than Musk on life on Earth, and potentially life off Earth too."[522][523]"""
    summary_template = """Given the {information} i want you to summarize it in the following criteria:
    1) Short Summary:
    2) Two main facts:
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model="llama3.2", temparture=0)

    chain = summary_prompt_template | llm

    response = chain.invoke({"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
