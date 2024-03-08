define v = Character("Guide", color="#83057dfb")
define g = Character("GAME OVER", color="#f10000dd")

label start:
    "L'air est lourd, vous ouvrez doucement les yeux..."
    scene pilules
    with fade
    "Devant vous une table où se trouve deux gélules et un verre d'eau."
    menu:
        "avaler la gélule bleue":
            jump gelule_bleue
        "avaler la gélule rouge":
            jump gelule_rouge
        "ne rien avaler":
            jump rien_avaler
    
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
    menu:
        "caresser le chien":
            jump chien
        "caresser le chat":
            jump chat

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
    menu:
        "passer la porte violette":
            jump porte_violette
        "passer la porte verte":
            jump porte_verte

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
    menu:
        "suivre la musique en passant par le portail bleu":
            jump musique
        "passer par le chemin de côté":
            jump chemin

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
    menu:
        "suivre l'odeur des fraises et monter":
            jump fraise
        "suivre l'odeur des roses et descendre":
            jump rose

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




