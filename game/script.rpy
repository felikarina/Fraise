define v = Character("Guide", color="#83057dfb")
define g = Character("GAME OVER", color="#f10000dd")

label start:
    "L'air est lourd, vous ouvrez doucement les yeux..."
    scene pilules
    with fade
    
    "Devant vous une table où se trouve deux gélules et un verre d'eau."
    call screen gelule
screen gelule:
    imagebutton:
        xpos 680
        ypos 630
        idle "geluleB.png"
        hover "geluleB2.png"
        tooltip "avaler la gélule bleue"
        action Jump("gelule_bleue")
    imagebutton:
        xpos 870
        ypos 620
        idle "geluleR.png"
        hover "geluleR2.png"
        tooltip "avaler la gélule rouge"
        action Jump("gelule_rouge")
    imagebutton:
        xpos 1100
        ypos 15
        idle "carafe.png"
        hover "carafe2.png"
        tooltip "juste boire de l'eau"
        action Jump("rien_avaler")
    
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" color "#ff0000" xpos 750 ypos 500
label gelule_bleue:
    scene pilulebleue
    with dissolve
    "À peine la gélule ingérée vous vous sentez mal, faible et vos jambes sont flageolantes."
    scene mort 
    with fade
    g "C'était du poison, vous n'avez pas fait long feu."
    scene black
    with dissolve
    return

label gelule_rouge:
    scene pilulerouge
    with dissolve
    "À peine la gélule ingérée vous vous sentez mal, faible et vos jambes sont flageolantes."
    scene mort 
    with fade
    g "C'était du poison, vous n'avez pas fait long feu."
    scene black
    with dissolve
    return

label rien_avaler:
    scene chienchat
    with fade
    "En examinant la pièce vous vous rendez compte que vous n'êtes pas seul."
    "Un chien et un chat vous observent intrigués par votre présence."
    call screen chienchat
screen chienchat:
    imagebutton:
        xpos 10
        ypos 10
        idle "chien.png"
        hover "chien2.png"
        tooltip "caresser le chien"
        action Jump("chien")
    imagebutton:
        xpos 1140
        ypos 10
        idle "chat.png"
        hover "chat2.png"
        tooltip "caresser le chat"
        action Jump("chat")
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" color "#ff0000" xpos 950 ypos 200
label chien:
    scene chien_enrage
    with dissolve
    "Le chien devint soudainement agressif et vous mord à la gorge."
    scene mort
    with fade
    g "Perdant trop de sang vous succombez."
    scene black
    with dissolve
    return

label chat:
    scene portes
    with fade
    "Le chat ronronne de plaisir, vous poursuivez votre chemin et tomber sur deux portes."
    "Vous entendez de la musique provenir de la porte verte de gauche, tandis que la porte violette de droite semble silencieuse."
    call screen porte
screen porte:
    imagebutton:
        xpos 500
        ypos 100
        idle "porteverte.png"
        hover "porteverte2.png"
        tooltip "passer la porte verte"
        action Jump("porte_verte")
    imagebutton:
        xpos 1000
        ypos 100
        idle "porteviolette.png"
        hover "porteviolette2.png"
        tooltip "passer la porte violette"
        action Jump("porte_violette")
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" color "#ff0000" xpos 750 ypos 950

label porte_violette: 
    scene porte_violette
    with dissolve
    "À peine vous poser un pied dans la pièce que des hommes vous frappent à la tête."
    scene mort
    with fade
    g "Vous perdez connaissance."
    scene black
    with dissolve
    return

label porte_verte:
    scene cour
    with fade
    "Vous atterrissez dans une petite cour extérieure."
    "Vous entendez la musique plus fortement, êtes-vous curieux d'en savoir l'origine ?"
    call screen cour
screen cour:
    imagebutton:
        xpos 1210
        ypos 1
        idle "portail.png"
        hover "portail2.png"
        tooltip "suivre la musique"
        action Jump("musique")
    imagebutton:
        xpos 1
        ypos 150
        idle "chemin.png"
        hover "chemin2.png"
        tooltip "prendre le chemin sur le côté"
        action Jump("chemin")
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" color "#ff0000" xpos 750 ypos 900


label musique:
    scene camion
    with fade
    "Le portail donnait directement sur la route et un chauffard vous renverse avec son camion"
    scene mort
    with fade
    g "Vous perdez proche de la fin."
    scene black
    with dissolve
    return

label chemin:
    scene escalier
    with fade
    "Vous débouchez sur un escalier, vous sentez comme une odeur de fraise venir de la droite et une odeur de rose venir de la gauche."
    call screen escalier
screen escalier:
    imagebutton:
        xpos 600
        ypos 200
        idle "haut.png"
        hover "haut2.png"
        tooltip "suivre l'odeur des fraises"
        action Jump("fraise")
    imagebutton:
        xpos 1050
        ypos 360
        idle "bas.png"
        hover "bas2.png"
        tooltip "suivre l'odeur des roses"
        action Jump("rose")
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" color "#ff0000" xpos 550 ypos 900


label fraise:
    scene fraise
    with fade
    "Vous découvrez un étalage de fraise, vous salivez et ne pouvez vous empêcher d'en manger."
    scene mort
    with fade
    g "Le propriétaire des fraises vous attrape et appelle la police, pas de chance."
    scene black
    with dissolve
    return

label rose:
    scene rose
    with fade
    "Vous découvrez un champ de rose et un sentiment de liberté et plénitude vous envahit."
    scene win 
    scene win2
    with dissolve
    scene win3
    with dissolve
    scene win4
    with dissolve
    scene win3
    with dissolve
    scene win4
    with dissolve
    scene win3
    with dissolve
    scene win4
    with dissolve
    "Bravo vous êtes arrivé à la fin du jeu."




