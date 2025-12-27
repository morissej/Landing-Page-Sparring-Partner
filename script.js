document.addEventListener('DOMContentLoaded', function() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const accordionItem = header.parentElement;
            
            // Toggle active class on current item
            accordionItem.classList.toggle('active');
            
            // Optional: Close other items (if you want only one open at a time)
            // Uncomment the lines below to enable accordion behavior (one open at a time)
            /*
            document.querySelectorAll('.accordion-item').forEach(item => {
                if (item !== accordionItem) {
                    item.classList.remove('active');
                }
            });
            */
        });
    });
});
