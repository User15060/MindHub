# CheatSheet Développement Web

Bienvenue sur ton CheatSheet Développement Web — ta référence rapide pour tout ce qui touche au HTML, CSS, JavaScript, et plus encore !

---

## 🚀 Pourquoi ce CheatSheet ?

Ce cheat sheet est conçu pour t’aider à retrouver rapidement les commandes, syntaxes, astuces et bonnes pratiques essentielles du développement web, sans perdre de temps dans des docs trop longues.

Que tu sois débutant ou développeur confirmé, tu y trouveras des exemples concrets et des rappels utiles.

---

## 🧠 Langages & Technologies disponibles

Explore les principaux langages proposés. Clique pour accéder au contenu dédié !

<div class="lang-carousel">
  <a href="python.md"><img src="images/logos/python.png" alt="Python"></a>
  <a href="csharp.md"><img src="images/logos/csharp.png" alt="C#"></a>
  <a href="cpp.md"><img src="images/logos/cpp.png" alt="C++"></a>
  <a href="c.md"><img src="images/logos/c.png" alt="C"></a>
  <a href="html.md"><img src="images/logos/html.png" alt="HTML"></a>
  <a href="css.md"><img src="images/logos/css.png" alt="CSS"></a>
  <a href="javascript.md"><img src="images/logos/js.png" alt="JavaScript"></a>
  <a href="java.md"><img src="images/logos/java.png" alt="Java"></a>
</div>

<style>
.lang-carousel {
  display: flex;
  overflow: hidden;
  gap: 20px;
  animation: scroll 20s linear infinite;
  padding: 20px 0;
}

.lang-carousel:hover {
  animation-play-state: paused;
}

.lang-carousel a img {
  height: 60px;
  transition: transform 0.3s ease;
  filter: grayscale(50%);
}

.lang-carousel a:hover img {
  transform: scale(1.2);
  filter: grayscale(0%);
}

@keyframes scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* Responsive */
@media (max-width: 768px) {
  .lang-carousel {
    flex-wrap: wrap;
    justify-content: center;
    animation: none;
  }
}
</style>
---

## 💡 Astuce du jour

Pour centrer un élément avec Flexbox, utilise simplement :

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

## 💬 Citation inspirante

> "Simplicity is the soul of efficiency." — Austin Freeman

---

## 🌐 Ressources utiles

- [MDN Web Docs](https://developer.mozilla.org) : la bible du développement web  
- [CSS-Tricks](https://css-tricks.com) : astuces et techniques CSS  
- [JavaScript.info](https://javascript.info) : guide complet JS moderne

---

## 🚧 À venir

- API REST & AJAX  
- Frameworks JS (React, Vue)  
- Tests unitaires & CI/CD

---

## 🤝 Contribuer

Ce cheat sheet est collaboratif ! Propose tes ajouts ou corrections sur [GitHub](https://github.com/tonrepo).

---

---

## 🎓 Tips pour bien étudier le développement web

<div style="max-width: 600px; margin: auto;">

<div id="tipSlides" style="border: 1px solid #ddd; padding: 20px; border-radius: 8px; font-size: 1.1em; min-height: 120px; display: flex; align-items: center; justify-content: center; transition: opacity 0.5s;">
  <!-- Le contenu des tips sera injecté ici -->
</div>

<div style="text-align: center; margin-top: 10px;">
  <button onclick="prevTip()" style="padding: 5px 12px; margin-right: 10px;">⬅️ Précédent</button>
  <button onclick="nextTip()" style="padding: 5px 12px;">Suivant ➡️</button>
</div>

</div>

<script>
  const tips = [
    "Fixe-toi des objectifs clairs : chaque jour, apprends un concept précis.",
    "Pratique beaucoup : écris du code, teste, expérimente.",
    "Utilise des projets concrets pour appliquer ce que tu apprends.",
    "N'hésite pas à relire et revoir plusieurs fois les notions difficiles.",
    "Fais des pauses régulières pour garder ta concentration et ta motivation.",
    "Participe à des communautés et discute avec d'autres développeurs.",
    "Documente ce que tu apprends, ça aide à mieux mémoriser.",
  ];

  let currentTip = 0;
  const tipDiv = document.getElementById('tipSlides');

  function showTip(index) {
    if(index < 0) index = tips.length - 1;
    if(index >= tips.length) index = 0;
    currentTip = index;
    tipDiv.style.opacity = 0;
    setTimeout(() => {
      tipDiv.textContent = tips[currentTip];
      tipDiv.style.opacity = 1;
    }, 300);
  }

  function nextTip() {
    showTip(currentTip + 1);
  }

  function prevTip() {
    showTip(currentTip - 1);
  }

  // Afficher le premier tip au chargement
  showTip(0);
</script>
