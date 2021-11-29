

$(document).ready(function() {

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

    const price = [];
    const qu = [];
    var sum = 0;
    $(".table_row").each(function(i){
        price[i] = $(this).find(".column-3").attr("value");
        qu[i] = $(this).find("#p-quantity").attr("value");
        sum += (parseInt(price[i]) * parseInt(qu[i]));
    });
    $(".subtotal").html(sum.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));

    const price_cart = [];
    const qu_cart = [];
    var sumCart = 0;
    $(".header-cart-item-info").each(function(i) {
        price_cart[i] = $(this).find("#price").html();
        qu_cart[i] = $(this).find("#stock").html();
        sumCart += (parseInt(price_cart[i]) * parseInt(qu_cart[i]));
    });
    $(".sub-total").html(sumCart.toLocaleString('it-IT', {style : 'currency', currency : 'VND'})); 
    
    var ship; 
    $(document).click(function() {
        $(".select2-selection__rendered").each(function(i) {
            if (i == 1) {
                ship = parseInt($(this).attr("title").slice($(this).attr("title").length - 6, $(this).attr("title").length));
                console.log(ship);
                $(".ship_cost").html(ship.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
                $(".total").html((ship+sum).toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
            }
        });
        
    }); 
    
    // Delete Django Ajax Call
    $("tr").find("#edit").each(function() {
        $(this).click(function(e){
            e.preventDefault();
            
            var id = $(this).closest("td").attr("value");
            $(this).closest("tr").remove();
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
    })
   
    $(".update-button").click(function(e) {
        e.preventDefault();
        
        var id = [];
        var title = [];
        var count = [];
        var price = [];
        var attr = [];
        $("tr").each(function(e) {  
            id[e] = $(this).find("td.text-center").closest("td").attr("value");
            title[e] = $(this).find("td.title").closest("td").attr("value");
            price[e] = $(this).find("td.price").closest("td").attr("value");
            attr[e] = $(this).find("td.product_attr").closest("td").attr("value");
            count[e] = $(this).find("input").val();
        });
    
        $.ajax({
            url: 'cart-data',
            data: {
                'id': JSON.stringify(id),
                'title': JSON.stringify(title),
                'price': JSON.stringify(price),
                'attr': JSON.stringify(attr),
                'count': JSON.stringify(count),
            },
            dataType: 'json',
            success: function (data) {
                $('.js-addcart-detail').modal('show');
            }
        })
    });

});

