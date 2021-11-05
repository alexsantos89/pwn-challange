new Vue({
  el: '#app',
  data: {
      fields: [
          'item_code',
          'product',
          'package',
          'available_units',
          'category',
          'last_updated',
          { key: 'quantity', label: 'Edit available quantity' }
      ],
      items: [
          { item_code: 'ACC1', product: 'Apple granny smith', package: '40 LB', available_units: 30, category: 'Fruits', last_updated: '2021-02-05 08:28:36'},
          { item_code: 'ACC1', product: 'Pineapple crownless', package: '7 CT', available_units: 60, category: 'Fruits', last_updated: '2021-02-03 19:49:33' },
          { item_code: 'ACC1', product: 'Banana green', package: '8 CT', available_units: 75, category: 'Fruits', last_updated: '2021-02-02 19:17:15' },
          { item_code: 'ACC2', product: 'Banana green tip', package: '40 LB', available_units: 15, category: 'Fruits', last_updated: '2021-02-02 09:46:33'},
      ],
      filter: null,
      filterOn: ['item_code', 'product', 'category'],
  },
  methods: {
      updateValue: function(index, event) {
          this.items[index].quantity = event
      },
  }
})