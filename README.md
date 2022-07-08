# jiekou_ceshi
Pytest+Excel+Allure接口自动化框架

此项目是基于Pytest集成Excel数据驱动的接口自动化框架，用Allure展示测试报告，运用接口关键字封装、Pytest参数化和JsonPath提取器实现多接口多参数的接口测试。
1、基于Python实现接口测试，运用requests、json、jsonpath、openpyxl库；
2、接口关键字封装+反射机制，动态生成接口请求;
3、Pytest参数化+Excel数据循环读取获取测试数据，应用setup实现Pytest用例预置；
4、使用allure装饰器生成报告，JsonPath提取器实现多接口参数关联。
