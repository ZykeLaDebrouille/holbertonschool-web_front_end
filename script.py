import os

def create_css_file(task_number, content):
    directory = "CSS_advanced/styles"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filename = f"{directory}/{task_number}-style.css"
    with open(filename, "w") as file:
        file.write(content)
    print(f"Created {filename}")

# Contenu de base pour le fichier 0
base_content = "/* No CSS for this task */"

# Tâches et contenu supplémentaire correspondant
tasks = [
    ("0", base_content),
    ("1", """
html {
    scroll-behavior: smooth;
}
"""),
    ("2", """
body {
    color: #161616;
}
a {
    color: #161616;
}
.visually-hidden {
    display: none;
}
.card-category,
.section-tagline {
    color: #D73953;
}
"""),
    ("3", """
:root {
    --color-primary: #d73953;
    --color-black: #090909;
    --color-white: #ffffff;
    --color-light-grey: #f3f3f3;
    --color-dark-grey: #353535;
    --text-color: var(--color-black);
}
body,
a {
    color: var(--text-color);
}
.card-category,
.section-tagline {
    color: var(--color-primary);
}
"""),
    ("4", """
:root {
    --font-family-base: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    --font-family-title: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
body {
    font-family: var(--font-family-base);
}
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-family-title);
}
"""),
    ("5", """
:root {
    --font-size-small: 1.2rem;
    --font-size-medium: 1.6rem;
    --font-size-large: 1.8rem;
    --font-size-x-large: 2.3rem;
    --font-size-xx-large: 4.8rem;
}
html {
    font-size: 62.5%;
}
body {
    font-size: var(--font-size-medium);
}
"""),
    ("6", """
:root {
    --font-weight-regular: 400;
    --font-weight-bold: 700;
}
body {
    font-weight: var(--font-weight-regular);
}
h1, h2, h3, h4, h5, h6 {
    font-weight: var(--font-weight-bold);
}
"""),
    ("7", """
:root {
    --font-family-base: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    --font-family-title: 'Raleway', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
"""),
   ("8", """
:root {
   --line-height-small: 1.2;
   --line-height-base: 1.5;
   --line-height-big: 1.8;
}
body {
   line-height: var(--line-height-base);
}
"""),
   ("9", """
a {
   text-decoration:none; 
} 
"""),
   ("10", """
.section-header {
   text-align:center; 
} 
"""),
   ("11", """
.section-tagline {
   font-family: var(--font-family-title);
   text-transform: uppercase; 
   font-weight: var(--font-weight-bold); 
} 
"""),
   ("12", """
.section-title {
   font-family: var(--font-family-title);
   font-size: var(--font-size-xx-large);
   font-weight: var(--font-weight-bold);
   margin: 0; /* Utilisation de la variable si nécessaire */
   color: var(--color-black); 
} 
"""),
   ("13", """
a[href] { 
   color :inherit; 
} 
a[href]:visited { 
   font-style :italic; 
} 
a[href]:hover { 
   text-decoration :underline; 
} 
a[href]:active { 
   background-color :var(--color-light-grey); 
}  
"""),
   ("14", """
@import url('https://necolas.github.io/normalize.css/latest/normalize.css');  
"""),
   ("15", """
*, *::before , *::after { box-sizing:border-box; }  
"""),
   ("16", """
.container { width :960px; margin-left:auto; margin-right:auto; }  
"""),
   ("17", """
:root {  
--section-padding :5rem 0;  
--section-header-padding :0 0 3rem;  
--section-body-padding :0 0 3rem;  
--section-footer-padding :3rem 0 0;  
--section-footer-align:center ;  
--footer-padding :5rem 0 1rem ;  
}  
.section { padding :var(--section-padding); }  
.section-header { padding :var(--section-header-padding); }  
.section-body { padding :var(--section-body-padding); }  
.section-footer { padding :var(--section-footer-padding); text-align :var(--section-footer-align) ; }  
.footer { padding :var(--footer-padding) ; }  
"""),
   ("18", """
.navbar-menu { float:right ; }  
.nav { margin :0; padding :0; list-style:none ; text-align:center ; }  
.nav .nav-item { 
   font-family :var(--nav-item-font-family) ; 
   font-weight :var(--nav-item-font-weight) ; 
   font-size :var(--nav-item-font-size) ; 
   letter-spacing :.04em ; 
   display:inline-block ; 
   margin-bottom :.3em ; 
}  
.nav .nav-link { display:block ; padding :.5em 1em ; }  
.nav .nav-link:hover { color :var(--nav-item-link-hover) ; }  

/* Variables pour le nav */
.root {  
--nav-item-font-family :'Raleway' , 'Helvetica Neue' , Helvetica , Arial , sans-serif ;  
--nav-item-font-weight:bold ;  
--nav-item-font-size :.16em ;  
--nav-item-letter-spacing :.04em ;  
--nav-item-display:inline-block ;  
--nav-item-margin :.3em auto .3em auto ;  
--nav-item-link-hover:#d73953 ;  
}   
"""),
   ("19", """
.row ul{ margin-left:auto;margin-right:auto;padding-left:auto;padding-right:auto;}  

.col-1-3{ width:.333%;float:left;padding:.5em;}  

.col-1-2{ width:.5%;float:left;padding:.5em;}  

.footer-copyright{ margin-left:auto;margin-right:auto;font-size:.12em;color:#090909;}  

.footer ul{ text-align:right;}   
"""),
   ("20", """
.row::after{ content:'';display:block;clear:left;}   
"""),
   ("21", """[class^='col-']{ float:left;padding:.5em;}   
"""),
   ("22", """[data-section-theme='dark']{ background-color:#090909;color:#ffffff;}   
"""),
   ("23", """.footer-address{ color:#ffffff;} .social-link{ display:block;} .social-link svg{ fill:#ffffff;}   
"""),
   ("24", """.card-services .card-title{ margin-left:auto;margin-right:auto;} .card-services a{ display:block;padding-left:.2em;padding-right:.2em;background-color:#f3f3f3;} .card-services a:hover{ color:#ffffff;background-color:#d73953;text-decoration:none;}   
"""),
   ("25", """:root{ 
--button-display:inline-block; 
--button-padding:.15em .30em; 
--button-border:.02rem solid var(#d73953); 
--button-color:#090909; 
--button-text-decoration:none; 
--button-font-size:.18em; 
--button-hover-color:#ffffff; 
--button-hover-text-decoration:none; 
--button-hover-background:#d73953;} 

.button{ display:inline-block;padding-left:.15em;padding-right:.30em;border:.02rem solid var(#d73953);color:#090909;text-decoration:none;font-size:.18em;} 

.button:hover{ color:#ffffff;text-decoration:none;background-color:#d73953;} 

[data-section-theme='dark'] .button{ color:#ffffff;}   
"""),
   ("26", """.card-testimonial{text-align:center;} .card-testimonial .card-avatar{ border-radius:.50%;width:.10em;height:.10em;} .card-testimonial cite{ display:block;padding-top:.10em;color:#d73953;}   
"""),
   ("27", """.section-hero{ background-size:.90rem auto;} .section-hero .section-title{ margin-bottom:.50rem;} .section-hero .section-inner{ padding-top:.10rem;padding-right:.40rem;padding-bottom:.20rem;padding-left:auto;}   
"""),("28","""
.header{
padding-top:.40rem;padding-bottom:auto;padding-left:auto;padding-right:auto;}
.header-logo-position,.header-logo-link-position,.header-logo-link-display,.header-logo-link-top,.header-logo-link-left,.header-logo-position-relative,.header-logo-link-position-absolute,.header-logo-link-display-inline-block,.header-logo-link-top-negative-one-em,.header-logo-link-left-zero{}
.header-logo-position-relative{}
.header-logo-link-position-absolute{}
.header-logo-link-display-inline-block{}
.header-logo-link-top-negative-one-em{}
.header-logo-link-left-zero{}
"""),("29","""
.nav-item-link-hover-white{} .nav.nav-link::before{}
"""),("30","""
.card-work.card-inner.card-image.card-title.card-inner.card-work.card-inner.card-work.card-inner.card-work.card-inner.card-work.card-inner.card-work.card-inner-card-work-card-inner-card-work-card-inner-card-work-card-inner-card-work-card-inner-card-work-card-inner-card-work-card-inner-card-work-card-inner{-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center;-webkit-transform-origin:center center{-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration:-moz-transition-duration{-ms-animation-timing-function:cubic-bezier(0.17,.67,.00,.01);}
"""),("31","""
.card-testimonial{-ms-animation-timing-function:cubic-bezier(0.17,.67,.00,.01);}
"""),("32","""
.card-testimonial{-ms-animation-timing-function:cubic-bezier(0.17,.67,.00,.01);}
"""
)]

# Initialiser le contenu avec la base
current_content = base_content

# Créer les fichiers pour chaque tâche en ajoutant progressivement le contenu
for task in tasks:
   task_number, additional_content = task
   current_content += additional_content
   create_css_file(task_number, current_content)

print("All CSS files have been created successfully.")