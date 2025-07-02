
window.addEventListener('scroll', function () {
    const navbar = document.getElementById('glass-navbar');
    if (window.scrollY > 10) {
      navbar.classList.add('navbar-hidden');
    } else {
      navbar.classList.remove('navbar-hidden');
    }
  });


// Remove Dropdown JS

  function showTab(tabName, el = null) {
    const technologies = {
      frontend: [
        { name: "TezJS", img: "/static/userapp/images/1.svg" },
        { name: "AngularJS", img: "/static/userapp/images/2.svg" },
        { name: "Vue.js", img: "/static/userapp/images/3.svg" },
        { name: "JavaScript", img: "/static/userapp/images/5.svg" },
        { name: "CSS3", img: "/static/userapp/images/6.svg" },
        { name: "HTML5", img: "/static/userapp/images/7.svg" }
      ],
      backend: [
        { name: "Node.js", img: "/static/userapp/images/8.svg" },
        { name: "Express.js", img: "/static/userapp/images/9.svg" },
        { name: "PHP", img: "/static/userapp/images/10.svg" },
        { name: "Python", img: "/static/userapp/images/11.svg" }
      ],
      mobile: [
        { name: "Flutter", img: "/static/userapp/images/12.svg" },
        { name: "React Native", img: "/static/userapp/images/13.svg" },
        { name: "Kotlin", img: "/static/userapp/images/14.svg" },
        { name: "Swift", img: "/static/userapp/images/15.svg" }
      ],
      database: [
        { name: "MySQL", img: "/static/userapp/images/16.svg" },
        { name: "MongoDB", img: "/static/userapp/images/17.svg" },
        { name: "PostgreSQL", img: "/static/userapp/images/18.svg" },
        { name: "Firebase", img: "/static/userapp/images/19.svg" }
      ],
      frameworks: [
        { name: "Laravel", img: "/static/userapp/images/20.svg" },
        { name: "Spring", img: "/static/userapp/images/21.svg" },
        { name: "Django", img: "/static/userapp/images/22.svg" }
      ],
      cloud: [
        { name: "AWS", img: "/static/userapp/images/23.svg" },
        { name: "Azure", img: "/static/userapp/images/25.svg" },
        { name: "Google Cloud", img: "/static/userapp/images/24.svg" }
      ],
      devops: [
        { name: "Docker", img: "/static/userapp/images/26.svg" },
        { name: "Kubernetes", img: "/static/userapp/images/27.svg" },
        { name: "Jenkins", img: "/static/userapp/images/28.svg" },
        { name: "GitHub Actions", img: "/static/userapp/images/29.svg" }
      ],
      ecommerce: [
        { name: "Magento", img: "/static/userapp/images/30.svg" },
        { name: "Shopify", img: "/static/userapp/images/31.svg" },
        { name: "WooCommerce", img: "/static/userapp/images/32.svg" }
      ],
      cms: [
        { name: "WordPress", img: "/static/userapp/images/33.svg" },
        { name: "Drupal", img: "/static/userapp/images/34.svg" },
        { name: "Joomla", img: "/static/userapp/images/35.svg" }
      ],
      platforms: [
        { name: "Windows", img: "/static/userapp/images/36.svg" },
        { name: "Linux", img: "/static/userapp/images/37.svg" },
        { name: "macOS", img: "/static/userapp/images/38.svg" }
      ]
    };
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
        if (el) {
          el.classList.add('active');
        } else {
          // Activate default tab
          const defaultTab = document.querySelector(`.tab[onclick*="${tabName}"]`);
          if (defaultTab) defaultTab.classList.add('active');
        }
        // Display tech items
        const container = document.getElementById("tabContent");
        container.innerHTML = "";
        technologies[tabName].forEach(tech => {
          container.innerHTML += `
            <div class="tech-item">
              <img src="${tech.img}" alt="${tech.name}" />
              <p>${tech.name}</p>
            </div>
          `;
        });
  }
  // Updated onclick in HTML (pass 'this')
  window.onload = () => showTab('frontend');


    // Check for Speech Recognition support
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.onresult = function(event) {
      const spokenText = event.results[0][0].transcript.toLowerCase().trim();
      console.log("Heard:", spokenText);
      if (spokenText.includes("start reading")) {
        speakText("Reading page content now.", () => {
          const pageText = document.body.innerText;
          speakText(pageText);
        });
      } else {
        speakText("Command not recognized. Please say start reading.");
      }
    };
    recognition.onerror = function(event) {
      console.error("Speech recognition error:", event.error);
      alert("Speech recognition error: " + event.error);
    };
    function startVoiceRecognition() {
      recognition.start();
    }
    function speakText(text, callback) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = "en-US";
      if (callback) {
        utterance.onend = callback;
      }
      speechSynthesis.cancel(); // Stop any current speech
      speechSynthesis.speak(utterance);
    }


    function myFunction() {
   var element = document.body;
   element.classList.toggle("dark-mode");
}