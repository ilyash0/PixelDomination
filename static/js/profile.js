document.addEventListener("DOMContentLoaded", function() {
  const canvasButtons = document.querySelectorAll('.btn-view-canvas');
  const createCanvasButton = document.querySelector('.btn-create-canvas');

  canvasButtons.forEach(button => {
    button.addEventListener('click', function() {
      const canvasId = this.closest('.profile__canvas-item').querySelector('img').alt;
      window.location.href = `/edit-canvas/${canvasId}`;  
    });
  });

  createCanvasButton.addEventListener('click', function() {
    window.location.href = '/create-canvas';  
  });
});