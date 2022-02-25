const myHeading = document.querySelector('h1');
myHeading.textContent = 'Adobe Transportation';




const myTitle = document.querySelector('title');
myTitle.textContent = 'New Title'

const button = document.querySelector('button');

button.onclick = function() {
  let name = prompt('What is your name?');
  alert('Hello ' + name + ', nice to see you!');
}

