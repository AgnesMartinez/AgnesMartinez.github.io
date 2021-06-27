import 'package:flutter/material.dart';

import 'dart:async' show Future;
import 'package:flutter/services.dart' show rootBundle;
import 'dart:convert';
import 'package:flutter/services.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter',
      routes: {
        "/": (context) => HomeScreen(),
        "/farmacos": (context) => FarmacosScreen(),
      },
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Menu Principal"),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Expanded(
              child: InkWell(
                  onTap: () => Navigator.pushNamed(context, "/farmacos"),
                  child: ColoredBox(
                    color: Colors.red.shade600,
                    child: Row(
                      children: [
                        SizedBox(
                          width: 20,
                        ),
                        Icon(
                          Icons.medication,
                          color: Colors.white,
                          size: 70,
                        ),
                        SizedBox(
                          width: 20,
                        ),
                        Text(
                          "Fármacos",
                          style: TextStyle(fontSize: 36, color: Colors.white),
                        ),
                        Spacer(),
                        Icon(
                          Icons.chevron_right,
                          color: Colors.white,
                          size: 50,
                        )
                      ],
                    ),
                  ))),
          Expanded(
              child: InkWell(
                  child: ColoredBox(
            color: Colors.pink.shade600,
            child: Row(
              children: [
                SizedBox(
                  width: 20,
                ),
                Icon(
                  Icons.calculate,
                  color: Colors.white,
                  size: 70,
                ),
                SizedBox(
                  width: 20,
                ),
                Text(
                  "Calculadora 1",
                  style: TextStyle(fontSize: 36, color: Colors.white),
                ),
                Spacer(),
                Icon(
                  Icons.chevron_right,
                  color: Colors.white,
                  size: 50,
                )
              ],
            ),
          ))),
          Expanded(
              child: InkWell(
                  child: ColoredBox(
            color: Colors.purple.shade600,
            child: Row(
              children: [
                SizedBox(
                  width: 20,
                ),
                Icon(
                  Icons.calculate,
                  color: Colors.white,
                  size: 70,
                ),
                SizedBox(
                  width: 20,
                ),
                Text(
                  "Calculadora 2",
                  style: TextStyle(fontSize: 36, color: Colors.white),
                ),
                Spacer(),
                Icon(
                  Icons.chevron_right,
                  color: Colors.white,
                  size: 50,
                )
              ],
            ),
          ))),
        ],
      ),
    );
  }
}

class FarmacosScreen extends StatefulWidget {
  @override
  _DefaultState createState() => _DefaultState();
}

class _DefaultState extends State<FarmacosScreen> {
  List _data = [];
  
  Future<void> readJson() async {
    var jsonText = await rootBundle.loadString("farmacos.json");
    var decoded = json.decode(jsonText);

    var data = [];
    var data2 =[];

    for(var item in decoded.keys) {
      data.add(item);
      data2.add(decoded[item]["Brand Name"]);
    }

    var finalData = [data, data2];

    setState(() => _data = finalData);
       
    
  }

  @override
  void initState() {
    super.initState();
    this.readJson();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Fármacos"),
      ),
      body: ListView.builder(
        itemCount: _data[0].length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text("${_data[0][index]}"),
            subtitle: Text("${_data[1][index]}"),
            trailing: Icon(Icons.chevron_right),
          );
        },
      ),
    );
  }
}
