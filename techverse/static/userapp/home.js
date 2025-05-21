window.addEventListener('scroll', function () {
    const navbar = document.getElementById('glass-navbar');
    if (window.scrollY > 80) {
      navbar.classList.add('navbar-hidden');
    } else {
      navbar.classList.remove('navbar-hidden');
    }
  });

document.addEventListener('DOMContentLoaded', function () {
  const serviceLink = document.getElementById('serviceDropdown');
  const dropdown = document.querySelector('.service-drop-div');

  if (serviceLink && dropdown) {
    // Toggle dropdown on mobile
    serviceLink.addEventListener('click', function (e) {
      const isMobile = window.innerWidth < 768;
      if (isMobile) {
        e.preventDefault();
        e.stopPropagation(); // Prevent closing immediately
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
      }
    });

    // Prevent closing dropdown when clicking inside it
    dropdown.addEventListener('click', function (e) {
      e.stopPropagation();
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function (e) {
      const isMobile = window.innerWidth < 768;
      if (isMobile && !e.target.closest('.nav-item')) {
        dropdown.style.display = 'none';
      }
    });
  }
});


  document.addEventListener('DOMContentLoaded', function () {
    const dropdownToggle = document.getElementById('industriesDropdown');
    const dropdownContent = document.getElementById('industriesDropContent');

    dropdownToggle.addEventListener('click', function (e) {
      const isMobile = window.innerWidth < 768;
      if (isMobile) {
        e.preventDefault(); // prevent link navigation
        dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
      }
    });

    // Optional: close dropdown on outside click
    document.addEventListener('click', function (e) {
      const isMobile = window.innerWidth < 768;
      if (isMobile && !e.target.closest('.nav-item')) {
        dropdownContent.style.display = 'none';
      }
    });
  });


  function showTab(tabName, el = null) {
    const technologies = {
      frontend: [
        { name: "TezJS", img: "https://img.icons8.com/ios/50/000000/source-code.png" },
        { name: "AngularJS", img: "https://img.icons8.com/color/48/angularjs.png" },
        { name: "ReactJS", img: "https://img.icons8.com/color/48/react-native.png" },
        { name: "Vue.js", img: "https://img.icons8.com/color/48/vue-js.png" },
        { name: "JavaScript", img: "https://img.icons8.com/color/48/javascript.png" },
        { name: "CSS3", img: "https://img.icons8.com/color/48/css3.png" },
        { name: "HTML5", img: "https://img.icons8.com/color/48/html-5.png" }
      ],
      backend: [
        { name: "Node.js", img: "https://img.icons8.com/color/48/nodejs.png" },
        { name: "Express.js", img: "https://img.icons8.com/ios/48/express-js.png" },
        { name: "PHP", img: "https://img.icons8.com/officel/48/php-logo.png" },
        { name: "Python", img: "https://img.icons8.com/color/48/python.png" }
      ],
      mobile: [
        { name: "Flutter", img: "https://img.icons8.com/color/48/flutter.png" },
        { name: "React Native", img: "https://img.icons8.com/color/48/react-native.png" },
        { name: "Kotlin", img: "https://img.icons8.com/color/48/kotlin.png" },
        { name: "Swift", img: "https://img.icons8.com/color/48/swift.png" }
      ],
      database: [
        { name: "MySQL", img: "https://img.icons8.com/ios-filled/50/mysql-logo.png" },
        { name: "MongoDB", img: "https://img.icons8.com/color/48/mongodb.png" },
        { name: "PostgreSQL", img: "https://img.icons8.com/color/48/postgreesql.png" },
        { name: "Firebase", img: "https://img.icons8.com/color/48/firebase.png" }
      ],
      frameworks: [
        { name: "Laravel", img: "https://img.icons8.com/ios-filled/50/laravel.png" },
        { name: "Spring", img: "https://img.icons8.com/color/48/spring-logo.png" },
        { name: "Django", img: "https://img.icons8.com/material-sharp/48/000000/django.png" }
      ],
      cloud: [
        { name: "AWS", img: "https://img.icons8.com/color/48/amazon-web-services.png" },
        { name: "Azure", img: "https://img.icons8.com/color/48/microsoft-azure.png" },
        { name: "Google Cloud", img: "https://img.icons8.com/color/48/google-cloud.png" }
      ],
      devops: [
        { name: "Docker", img: "https://img.icons8.com/color/48/docker.png" },
        { name: "Kubernetes", img: "https://img.icons8.com/color/48/kubernetes.png" },
        { name: "Jenkins", img: "https://img.icons8.com/color/48/jenkins.png" },
        { name: "GitHub Actions", img: "https://img.icons8.com/glyph-neue/48/github.png" }
      ],
      ecommerce: [
        { name: "Magento", img: "https://img.icons8.com/color/48/magento.png" },
        { name: "Shopify", img: "https://img.icons8.com/color/48/shopify.png" },
        { name: "WooCommerce", img: "https://img.icons8.com/color/48/woocommerce.png" }
      ],
      cms: [
        { name: "WordPress", img: "https://img.icons8.com/color/48/wordpress.png" },
        { name: "Drupal", img: "https://img.icons8.com/color/48/drupal.png" },
        { name: "Joomla", img: "https://img.icons8.com/color/48/joomla.png" }
      ],
      platforms: [
        { name: "Windows", img: "https://img.icons8.com/color/48/windows-10.png" },
        { name: "Linux", img: "https://img.icons8.com/color/48/linux.png" },
        { name: "macOS", img: "https://img.icons8.com/ios/48/mac-os.png" }
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