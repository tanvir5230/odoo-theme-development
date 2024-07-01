const quill = new Quill("#description", {
  theme: "snow",
});

// Handle form submission
function handleSubmit(event) {
  // Prevent default form submission
  event.preventDefault();

  const html = quill.getSemanticHTML();

  console.log(html);
}
