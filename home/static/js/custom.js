function getDataAjax() {
    
    var address = $("[name='address']").val() + " " + $("[name='phuong']").val() + " " + $("[name='district']").val() + " " + $("[name='city']").val();
    var info = $("[name='first-name']").val() + " " + $("[name='last-name']").val();
    var phone = $("[name='phone']").val();
    $.ajax({
        url: 'payment',
        data: {
            address: JSON.stringify(address),
            info: JSON.stringify(info),
            phone: JSON.stringify(phone),
            ship: JSON.stringify($("[name='district']").val()),
        },
        dataType: 'json',
        success: function() {
            console.log(address);
        }
    })
}

$(document).ready(function() {

    var price = [];
    var qu = [];
    var sum = 0;
    $(".table_row").each(function(i){
        price[i] = $(this).find(".column-3").attr("value");
        qu[i] = $(this).find("#p-quantity").attr("value");
        sum += (parseInt(price[i]) * parseInt(qu[i]));
    });
    $(".subtotal").html(sum.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));

    var total;
    $("table").each(function(){
      total = 0;
      $(this).find(".records").each(function(e){
        total += parseInt($(this).find("#amount").html()) * parseInt($(this).find("#price").html()) ;
      });
      $(this).find("#total-table").html(total.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
    });

    var tot = 0;
    $(".bill").each(function(i){
        var price = $(this).find(".price").html();
        var qu = $(this).find(".count").html();
        $(this).find(".subto").html((parseInt(price) * parseInt(qu)).toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
        tot += parseInt(price) * parseInt(qu);
    });
    var ship = parseInt($(".text-ship").html());
    $(".text-ship").html(ship.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
    $(".text-invoice-price").html(tot.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
    $(".text-total").html((tot+ship).toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));

    const price_cart = [];
    const qu_cart = [];
    var sumCart = 0;
    $(".header-cart-item-info").each(function(i) {
        price_cart[i] = $(this).find("#price").html();
        qu_cart[i] = $(this).find("#stock").html();
        sumCart += (parseInt(price_cart[i]) * parseInt(qu_cart[i]));
    });
    $(".sub-total").html(sumCart.toLocaleString('it-IT', {style : 'currency', currency : 'VND'})); 
    
    // Delete Django Ajax Call
    
    $("tr").find("#edit").each(function() {
        $(this).click(function(e){
            e.preventDefault();

            var id = $(this).closest("td").attr("value");
            $(this).closest("tr").remove();

            qu = [];
            price = [];
            sum = 0;
            $(".table_row").each(function(i){
                price[i] = $(this).find(".column-3").attr("value");
                qu[i] = $(this).find("#p-quantity").attr("value");
                sum += (parseInt(price[i]) * parseInt(qu[i]));
            });
            $(".subtotal").html(sum.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));

            $.ajax({
                url: 'delete',
                data: {
                    'id': id,
                },
                success: function(data) {
                    if (data.deleted){
                        console.log(data.id);
                    }
                },
            });
        });
    });

    $(".update-button").click(function(e) {
        
        e.preventDefault();
        
        var id = [];
        // var title = [];
        var count = [];
        // var price = [];
        // var attr = [];
        $("tr").each(function(e) {  
            id[e] = $(this).find("td.text-center").closest("td").attr("value");
            // title[e] = $(this).find("td.title").closest("td").attr("value");
            // price[e] = $(this).find("td.price").closest("td").attr("value");
            // attr[e] = $(this).find("td.product_attr").closest("td").attr("value");
            count[e] = $(this).find("input").val(); 
        });
        
        $.ajax({
            url: 'cart-data',
            data: {
                'id': JSON.stringify(id),
                // 'title': JSON.stringify(title),
                // 'price': JSON.stringify(price),
                // 'attr': JSON.stringify(attr),
                'count': JSON.stringify(count),
            },
            dataType: 'json',
            success: function (data) {
                $('.js-addcart-detail').modal('show');
            }
        });

        qu = [];
        price = [];
        sum = 0;
        $(".table_row").each(function(i){
            price[i] = $(this).find(".column-3").attr("value");
            qu[i] = $(this).find("#p-quantity").val();
            sum += (parseInt(price[i]) * parseInt(qu[i]));
        });
        $(".subtotal").html(sum.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
    });

    // Render the PayPal button into #paypal-button-container
    
    paypal.Buttons({
        
        style: {
            color:  'blue',
            shape:  'rect',
            label:  'pay',
            height: 40
        },

        // Set up the transaction
        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: (parseFloat($(".total").val())/22694.9185).toFixed(2)
                    }
                }]
            });
        },

        // Finalize the transaction
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(details) {
                // Show a success message to the buyer
                alert('Transaction completed by ' + details.payer.name.given_name + '!');
                $(".table_row").each(function() {
                    $(this).remove();
                });
                getDataAjax();
            });
        }
    }).render('#paypal-button-container');

    var ship; 
    $(document).click(function() {
        $(".select2-selection__rendered").each(function(i) {
            if (i == 1) {
                ship = parseInt($(this).attr("title").slice($(this).attr("title").length - 6, $(this).attr("title").length));
                $(".ship_cost").html(ship.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
                $(".total").html((ship+sum).toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
            }
        });
    }); 
    $(".total").val(ship+sum);
});

