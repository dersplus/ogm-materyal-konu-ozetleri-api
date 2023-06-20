
# OGM Materyal Konu Özetleri API

Dersplus API'nı kullanarak https://ogmmateryal.eba.gov.tr/konu-ozetleri adresinde yayınlanan konu özetlerini PHP, NodeJs ve Python örneklerini kullanarak çekebilirsiniz. API kullanımı aşağıda verilmiştir.


## API Kullanımı

#### Konu özetlerinde arama yap

```http
  GET https://api.dersplus.net/ogm/konu-ozetleri/search
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Gerekli**. Arama parametreniz. |

#### Sınıf düzeylerini getir

```http
  GET https://api.dersplus.net/ogm/konu-ozetleri/list-class
```
| Parametre almaz |
| :-------- |

#### Sınıfa göre konu özetlerini getir

```http
  GET https://api.dersplus.net/ogm/konu-ozetleri/fetch-by-class
```

| Parametre | Tip     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Gerekli**. Bir üsteki URL'den aldığınız sınıfın ID'si. |

