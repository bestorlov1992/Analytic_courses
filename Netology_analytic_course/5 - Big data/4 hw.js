// 3. Вставить 4 документа по товарам на сайте. Атрибуты:
// a. Название
// b. Категория (2 товара из одной категории, 2 товара из другой)
// c. Цена
// d. Количество товаров на складе
// db.collection.insert(
//   [
//     {
//       name: "milk",
//       category: "products",
//       price: 100,
//       qnt: 1000
//     },
//     {
//       name: "bread",
//       category: "products",
//       price: 50,
//       qnt: 2000
//     },
//     {
//       name: "tv",
//       category: "electronics",
//       price: 10000,
//       qnt: 100
//     },
//     {
//       name: "notebook",
//       category: "electronics",
//       price: 30000,
//       qnt: 300
//     }
//   ]
// )

// 4. Рассчитать остаточную стоимость товаров в каждой категории (сумма цены, умноженной на остаток)
// db.collection.aggregate({
//   "$project": {
//     total: {
//       "$multiply": [
//         "$price",
//         "$qnt"
//       ]
//     },
//     category: 1
//   }
// },
// {
//   "$group": {
//     "_id": "$category",
//     "residue": {
//       $sum: "$total"
//     }
//   }
// })
// 5. Уменьшить количество товара на 1
// db.collection.updateMany({},
// {
//   "$inc": {
//     "qnt": -1
//   }
// })

// 6. Вывести top-2 самых дорогих товара
//db.collection.aggregate({
//   "$project": {
//     _id: 0
//   }
// },
// {
//   "$sort": {
//     price: -1
//   }
// },
// {
//   "$limit": 2
// })