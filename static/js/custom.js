$(document).ready(function () {

    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input');
        var value = parseInt(inc_value.val(), 10);
        value = isNaN(value) ? 0 : value;

        if (value < 10) {
            value++;
            inc_value.val(value);
        }
    });

    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input');
        var value = parseInt(inc_value.val(), 10);
        value = isNaN(value) ? 0 : value;

        if (value > 0) { // Change the condition to value > 0 to prevent decrementing below zero
            value--;
            inc_value.val(value);
        }
    });
});
