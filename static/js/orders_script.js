window.onload = function () {
    let _quantity, _price, orderitem_num, delta_quantity, orderitem_quntity, delta_cost;
    let  quantity_arr = [],
         price_arr = [],
         total_forms = parseInt($('input[name=orderitems-TOTAL_FORMS]').val()),
         order_total_quantity = parseInt($('.order_total_quantity').text()) || 0,
         order_total_price = parseFloat($('.order_total_cost').text()) || 0;
    for (let i=0; i < total_forms; i++){
        _quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',' , '.'));

        quantity_arr[i] = _quantity;
        if(_price){
            price_arr[i] = _price;
        } else {
           price_arr[i] = 0;
        }
    }

    $('.order_form').on('click', 'input[type=number]', function(){
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity'));
        if(price_arr[orderitem_num]){
            orderitem_quntity = parseInt(target.value);
            delta_quantity = orderitem_quntity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quntity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    });

        $('.order_form').on('click', 'input[type=checkbox]', function(){
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE'));
        if(target.checked){
            delta_quantity = -quantity_arr[orderitem_num];
        }else {
            delta_quantity = quantity_arr[orderitem_num];
        }
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        });

$('.order_form select').change(function (event) {
        let target = event.target;
        let orderitemNum = parseInt(target.name.replace('orderitems-', '').replace(
            '-product', ''));
        let orderitemProductPk = target.options[target.selectedIndex].value;
        console.log(orderitemProductPk)

        if (orderitemProductPk) {
            $.ajax({
                url: "products/product/" + orderitemProductPk + "/price/",
                success: function (data) {
                    // console.log('get product price', data);
                    if (data.price) {
                        priceArr[orderitemNum] = parseFloat(data.price);
                        if (isNaN(quantityArr[orderitemNum])) {
                            quantityArr[orderitemNum] = 0;
                        }
                        let priceHtml = '<span>' +
                            data.price.toString().replace('.', ',') +
                            '</span> &#8381;';
                        let currentTr = $('.order_form table').find('tr:eq(' + (orderitemNum + 1) + ')');

                        currentTr.find('td:eq(2)').html(priceHtml);

                        if (isNaN(currentTr.find('input[type="number"]').val())) {
                            currentTr.find('input[type="number"]').val(0);
                        }
                        orderSummaryRecalc();
                    }
                },
            });
        }
    });


    function orderSummaryUpdate(orderitem_price, delta_quantity){
            delta_cost = orderitem_price * delta_quantity;
            order_total_price = Number((order_total_price + delta_cost).toFixed(2));
            order_total_quantity = order_total_quantity + delta_quantity;


            $('.order_total_quantity').text(order_total_quantity.toString());
            $('.order_total_cost').text(order_total_price.toString());
    }
    function orderSummaryRecalc() {
    orderTotalQuantity = 0;
    orderTotalCost = 0;

    for (let i = 0; i < totalForms; i++) {
        orderTotalQuantity += quantityArr[i];
        orderTotalCost += quantityArr[i] * priceArr[i];
    }
    $orderTotalQuantityDOM.html(orderTotalQuantity.toString());
    $('.order_total_cost').html(Number(orderTotalCost.toFixed(2)).toString());
}

    $('.formset_row').formset({
       addText: 'добавить продукт',
       deleteText: 'удалить',
       prefix: 'orderitems',
       removed: deleteOrderItem
    });
    function deleteOrderItem(row) {
       let target_name = row[0].querySelector('input[type="number"]').name;
       orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''));
       delta_quantity = -quantity_arr[orderitem_num];
       orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    }


};