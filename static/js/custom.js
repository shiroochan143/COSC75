$(document).ready(function () {
    console.log("Jquery loaded successfully")
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
        alert("button is clicked");
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input');
        var value = parseInt(inc_value.val(), 10);
        value = isNaN(value) ? 0 : value;

        if (value > 0) { // Change the condition to value > 0 to prevent decrementing below zero
            value--;
            inc_value.val(value);
        }
    });

    $('delete-cart-item').click(function (e ){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url : "http://localhost:8000/remove-cart-item/",
            data: {
                'product_id' : product_id,
                csrfmiddlewaretoken : token
            },
            success : function(response){
                console.log(response)
            }
        });
    });
});


