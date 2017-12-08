package com.ryuseongbin.meomeog;

import android.Manifest;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by 민지 on 2017-12-05.
 */

public class Recommend extends AppCompatActivity {
    private Button button_back;
    private Button button_go;
    private Button button5;
    private Button button6;
    private Button button7;

    LocationManager locationManager;
    LocationListener locationListener;

    Intent intent;

    boolean locchange = false;
    double latitude = 0.0, longitude = 0.0;
    boolean canReadLocation = false;
    private static final int REQUEST_CODE_LOCATION = 2;

    int r1 = 0, r2 = 0, r3 = 0;
    double s1 = 0.0, s2 = 0.0, s3 = 0.0;
    int c1 = 0, c2 = 0, c3 = 0;
    String rest1, rest2, rest3;

    String jsonStr;
    String result;
    private class JSONlib {
        String gender;
        int age, pref_new_rest, pref_dist;
        double longitute, latitute;
        int kr, ch, meat, soup, jp, fast, flour, chicken, pizza, noodle, western;
        int sashimi;

        public JSONlib(String gender, int age, int pref_new_rest, int pref_dist, double longitute, double latitute, int kr, int ch, int meat, int soup, int jp, int fast, int flour, int chicken, int pizza,
                       int noodle, int western, int sashimi) {
            this.gender = gender;
            this.age = age;
            this.pref_dist = pref_dist;
            this.pref_new_rest = pref_new_rest;
            this.longitute = longitute;
            this.latitute = latitute;
            this.kr = kr;
            this.ch = ch;
            this.meat = meat;
            this.soup = soup;
            this.jp = jp;
            this.fast = fast;
            this.flour = flour;
            this.chicken = chicken;
            this.pizza = pizza;
            this.noodle = noodle;
            this.western = western;
            this.sashimi = sashimi;
        }

        public String buildJSON() {
            JSONObject info = new JSONObject();
            try{
                info.put("gender", gender);
                info.put("age", age);
                info.put("pref_dist", pref_dist);
                info.put("pref_new_rest", pref_new_rest);
                info.put("long", longitute);
                info.put("lat", latitute);
                info.put("kr", kr);
                info.put("ch", ch);
                info.put("meat", meat);
                info.put("soup", soup);
                info.put("jp", jp);
                info.put("fast", fast);
                info.put("flour", flour);
                info.put("chicken", chicken);
                info.put("pizza", pizza);
                info.put("noodle", noodle);
                info.put("western", western);
                info.put("sashimi", sashimi);
            } catch(JSONException e){
                e.printStackTrace();
            }

            String jsoninfo = info.toString();

            return jsoninfo;
        }
    }


    private Location getMyLocation(){
        Log.d("GET LOC", "getMyLocation");

        Location currloc = null;
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // 사용자 권한 요청
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, REQUEST_CODE_LOCATION);
        }
        else {
            Log.d("GET LOC", "permission accepted");
            locationManager = (LocationManager) Recommend.this.getSystemService(LOCATION_SERVICE);
            locationListener = new LocationListener() {
                public void onLocationChanged(Location location) {
                    latitude = location.getLatitude();
                    longitude = location.getLongitude();
                    Log.d("GET LOC LISNTENER", "location changed  (" + latitude + ", " + longitude + ")");
                    locchange = true;
                }

                public void onStatusChanged(String provider, int status, Bundle extras) {
                }

                public void onProviderEnabled(String provider) {
                }

                public void onProviderDisabled(String provider) {
                }
            };

            locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 0, 0, locationListener);
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, locationListener);

            String locationPrivider = LocationManager.NETWORK_PROVIDER;

            currloc = locationManager.getLastKnownLocation(locationPrivider);
            if(currloc != null){
                longitude = currloc.getLongitude();
                latitude = currloc.getLatitude();

                Log.d("GET LOC", "(" + longitude + ", " + latitude + ")");
            }
        }

        return currloc;
    }

    public void onRequestPermissionResult(int requestCode, String[] permissions, int[] grantResults){
        if (requestCode == REQUEST_CODE_LOCATION) {
            if (grantResults.length == 1 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
// success!
                Location userLocation = getMyLocation();
                if( userLocation != null ) {
                    double latitude = userLocation.getLatitude();
                    double longitude = userLocation.getLongitude();
                }
                canReadLocation = true;
            } else {
// Permission was denied or request was cancelled
                canReadLocation = false;
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommend);
        button_back = (Button) findViewById(R.id.bt_back);
        button_go = (Button) findViewById(R.id.bt_go);
        button5 = (Button) findViewById(R.id.button5);
        button6 = (Button) findViewById(R.id.button6);
        button7 = (Button) findViewById(R.id.button7);

        intent = new Intent(Recommend.this, MomoActivity.class);

        SharedPreferences prefb = getSharedPreferences("pref", MODE_PRIVATE);
        String gender = prefb.getString("gender", "");
        int age = Integer.parseInt(prefb.getString("age", ""));     // Fill this part
        int kr = Integer.parseInt(prefb.getString("hansick", ""));
        int ch = Integer.parseInt(prefb.getString("jungsick", ""));
        int meat = Integer.parseInt(prefb.getString("gogi", ""));
        int soup = Integer.parseInt(prefb.getString("goongmul", ""));
        int jp = Integer.parseInt(prefb.getString("ilsick", ""));
        int fast = Integer.parseInt(prefb.getString("fastfood", ""));
        int flour = Integer.parseInt(prefb.getString("boonsick", ""));
        int chicken = Integer.parseInt(prefb.getString("chicken", ""));
        int pizza = Integer.parseInt(prefb.getString("pizza", ""));
        int noodle = Integer.parseInt(prefb.getString("noodle", ""));
        int sashimi = Integer.parseInt(prefb.getString("livefish", ""));
        int western = Integer.parseInt(prefb.getString("yangsick", ""));
        int pref_new_ret = Integer.parseInt(prefb.getString("new", ""));
        int pref_dist = Integer.parseInt(prefb.getString("distance", ""));

        getMyLocation();
        // while(!locchange){}
        if(gender.equals("남자"))     gender = "M";
        else            gender = "F";

        Log.d("Recommend", "(" + latitude + ", " + longitude + ")");
        JSONlib json = new JSONlib(gender, age, pref_new_ret, pref_dist, longitude, latitude, kr, ch, meat, soup, jp, fast, flour, chicken, pizza, noodle, western, sashimi);
        jsonStr = json.buildJSON();

        Log.d("Recommend", jsonStr);
        new Thread(){
            @Override
            public void run() {
                try {
                    Log.d("Network Thread", "Start HTTP URL Request");
                    URL url = new URL("http://115.145.179.194:9999");
                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();

                    conn.setRequestMethod("POST");
                    conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

                    conn.setRequestProperty("Content-Language", "en-US");

                    conn.setDoOutput(true);
                    conn.setDoInput(true);

                    DataOutputStream wr = new DataOutputStream(conn.getOutputStream());

                    jsonStr = "data=" + jsonStr;

                    wr.writeBytes(jsonStr);

                    InputStream is = conn.getInputStream();
                    BufferedReader rd = new BufferedReader(new InputStreamReader(is));
                    StringBuilder res = new StringBuilder();
                    String line;

                    while ((line = rd.readLine()) != null) {
                        res.append(line);
                        res.append("\n");
                    }

                    result = res.toString();
                    Log.d("Recommend", res.toString());
                    try{
                        JSONObject jsonObject = new JSONObject(result);

                        r1 = jsonObject.getInt("1name");
                        r2 = jsonObject.getInt("2name");
                        r3 = jsonObject.getInt("3name");

                        s1 = jsonObject.getDouble("1score");
                        s2 = jsonObject.getDouble("2score");
                        s3 = jsonObject.getDouble("3score");

                        c1 = jsonObject.getInt("1cat");
                        c2 = jsonObject.getInt("2cat");
                        c3 = jsonObject.getInt("3cat");

                        rest1 = RestName.Restaurant[r1 - 1];
                        rest2 = RestName.Restaurant[r2 - 1];
                        rest3 = RestName.Restaurant[r3 - 1];

                        Log.d("NetWork Thread", rest1 + " " + rest2 + " " + rest3);
                        Log.d("NetWork Thread",  s1 + " " + s2 + " " + s3);
                        Log.d("NetWork Thread", c1 + " " + c2 + " " + c3);

                    } catch(JSONException e){
                        e.printStackTrace();
                    }
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();

        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                intent.putExtra("name", rest1);
                intent.putExtra("category", RestName.Category[c1]);
                intent.putExtra("grade", String.format("%.3f", s1));

                startActivity(intent);
            }
        });
        button6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                intent.putExtra("name", rest2);
                intent.putExtra("category", RestName.Category[c2]);
                intent.putExtra("grade", String.format("%.3f", s2));
                startActivity(intent);
            }
        });
        button7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                intent.putExtra("name", rest3);
                intent.putExtra("category", RestName.Category[c3]);
                intent.putExtra("grade", String.format("%.3f", s3));
                startActivity(intent);
            }
        });

        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
        button_go.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
            new Thread(){
                @Override
                public void run() {
                    try {
                        Log.d("Network Thread", "Start HTTP URL Request");
                        URL url = new URL("http://115.145.179.194:9999");
                        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

                        conn.setRequestMethod("POST");
                        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

                        conn.setRequestProperty("Content-Language", "en-US");

                        conn.setDoOutput(true);
                        conn.setDoInput(true);

                        DataOutputStream wr = new DataOutputStream(conn.getOutputStream());

                        wr.writeBytes(jsonStr);

                        InputStream is = conn.getInputStream();
                        BufferedReader rd = new BufferedReader(new InputStreamReader(is));
                        StringBuilder res = new StringBuilder();
                        String line;

                        while ((line = rd.readLine()) != null) {
                            res.append(line);
                            res.append("\n");
                        }

                        result = res.toString();
                        Log.d("Recommend", res.toString());
                        try{
                            JSONObject jsonObject = new JSONObject(result);

                            r1 = jsonObject.getInt("1name");
                            r2 = jsonObject.getInt("2name");
                            r3 = jsonObject.getInt("3name");

                            s1 = jsonObject.getDouble("1score");
                            s2 = jsonObject.getDouble("2score");
                            s3 = jsonObject.getDouble("3score");

                            c1 = jsonObject.getInt("1cat");
                            c2 = jsonObject.getInt("2cat");
                            c3 = jsonObject.getInt("3cat");

                            rest1 = RestName.Restaurant[r1 - 1];
                            rest2 = RestName.Restaurant[r2 - 1];
                            rest3 = RestName.Restaurant[r3 - 1];

                            Log.d("NetWork Thread", rest1 + " " + rest2 + " " + rest3);
                            Log.d("NetWork Thread",  s1 + " " + s2 + " " + s3);
                            Log.d("NetWork Thread", c1 + " " + c2 + " " + c3);

                        } catch(JSONException e){
                            e.printStackTrace();
                        }
                    } catch (MalformedURLException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }.start();
            }
        });
    }
}