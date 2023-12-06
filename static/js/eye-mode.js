document.addEventListener('DOMContentLoaded', function () {
    var modeToggle = document.getElementById('mode-toggle');
    var modeIcon = document.getElementById('mode-icon');

    if (!modeToggle || !modeIcon) {
        console.error('Could not find mode-toggle or mode-icon elements.');
        return;
    }

    modeToggle.addEventListener('click', function () {
        console.log('Button clicked!');
        var currentSrc = modeIcon.src;
        console.log('Current source:', currentSrc);

        if (currentSrc.includes(window.staticLightModePath)) {
            console.log('Switching to dark mode icon now im black');
            modeIcon.src = window.staticDarkModePath;
        } else {
            console.log('Switching to light mode icon cuz im white');
            modeIcon.src = window.staticLightModePath;
        }
    });
});
