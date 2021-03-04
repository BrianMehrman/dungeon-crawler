<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.4" tiledversion="1.4.3" name="ground" tilewidth="32" tileheight="32" tilecount="360" columns="15">
 <editorsettings>
  <export target="../../ground..json" format="json"/>
 </editorsettings>
 <image source="../images/tilesets/1.png" width="480" height="768"/>
 <terraintypes>
  <terrain name="grass-01" tile="16"/>
  <terrain name="grass-02" tile="138"/>
  <terrain name="dirt--01" tile="156"/>
  <terrain name="farm-01" tile="148"/>
  <terrain name="sand-01" tile="189"/>
  <terrain name="water-01" tile="8"/>
  <terrain name="lava-01" tile="26"/>
  <terrain name="wall-01" tile="184"/>
  <terrain name="wall-02" tile="323"/>
  <terrain name="swamp-01" tile="281"/>
 </terraintypes>
 <tile id="0" type="Grass" terrain=",,,0">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="1" type="Grass" terrain=",,0,0">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="2" type="Grass" terrain=",,0,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="3" type="Grass" terrain="0,0,0,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="4" type="Grass" terrain="0,0,,0">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="5" type="Water" terrain=",,,5">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="6" type="Water" terrain=",,5,5">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="7" type="Water" terrain=",,5,">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="8" type="WaterEdge" terrain="5,5,5,">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="9" type="WaterEdge" terrain="5,5,,5">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="10" type="Lava" terrain=",,,6">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="11" type="Lava" terrain=",,6,6">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="12" type="Lava" terrain=",,6,">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="13" type="Lava" terrain="6,6,6,">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="14" type="Lava" terrain="6,6,,6">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="15" type="Grass" terrain=",0,,0">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="16" type="Grass" terrain="0,0,0,0">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="17" type="Grass" terrain="0,,0,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="18" type="Grass" terrain="0,,0,0">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="19" type="Grass" terrain=",0,0,0">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="20" type="Water" terrain=",5,,5">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="21" type="WaterOpen" terrain="5,5,5,5">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="22" type="Water" terrain="5,,5,">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="23" type="WaterEdge" terrain="5,,5,5">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="24" type="WaterEdge" terrain=",5,5,5">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="25" type="Lava" terrain=",6,,6">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="26" type="Lava" terrain="6,6,6,6">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="27" type="Lava" terrain="6,,6,">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="28" type="Lava" terrain="6,,6,6">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="29" type="Lava" terrain=",6,6,6">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="30" type="Grass" terrain=",0,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="31" type="Grass" terrain="0,0,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="32" type="Grass" terrain="0,,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="33">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="34">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="35" type="Water" terrain=",5,,">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="36" type="Water" terrain="5,5,,">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="37" type="Water" terrain="5,,,">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="38">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="39">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="40" type="Lava" terrain=",6,,">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="41" type="Lava" terrain="6,6,,">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="42" type="Lava" terrain="6,,,">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="43">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="44">
  <properties>
   <property name="cost" type="int" value="100"/>
  </properties>
 </tile>
 <tile id="45" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="46" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="47" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="48" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="49" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="50" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="51" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="52" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="53" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="54" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="55" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="56" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="57" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="58" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="59" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="60" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="61" type="WaterOpen">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="62" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="63" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="64" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="65" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="66" type="WaterOpen">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="67" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="68" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="69" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="70" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="71" type="WaterOpen">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="72" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="73" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="74" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="75" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="76" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="77" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="78" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="79" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="80" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="81" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="82" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="83" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="84" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="85" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="86" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="87" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="88" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="89" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="90" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="91" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="92" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="93" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="94" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="95" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="96" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="97" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="98" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="99" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="100" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="101" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="102" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="103" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="104" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="105" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="106" type="WaterOpen">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="107" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="108" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="109" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="110" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="111" type="WaterOpen">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="112" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="113" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="114" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="115" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="116" type="WaterOpen">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="117" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="118" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="119" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="120" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="121" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="122" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="123" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="124" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="125" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="126" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="127" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="128" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="129" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="130" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="131" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="132" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="133" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="134" type="WaterEdge">
  <properties>
   <property name="cost" type="int" value="200"/>
  </properties>
 </tile>
 <tile id="135" type="Grass" terrain=",,,1">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="136" type="Grass" terrain=",,1,1">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="137" type="Grass" terrain=",,1,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="138" type="Grass" terrain="1,1,1,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="139" type="Grass" terrain="1,1,,1">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="140" type="Dirt" terrain=",,,2">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="141" type="Dirt" terrain=",,2,2">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="142" type="Dirt" terrain=",,2,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="143" type="Dirt" terrain="2,2,2,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="144" type="Dirt" terrain="2,2,,2">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="145" type="Farm" terrain=",,,3">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="146" type="Farm" terrain=",,3,3">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="147" type="Farm" terrain=",,3,">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="148" type="Farm" terrain="3,3,3,">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="149" type="Farm" terrain="3,3,,3">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="150" type="Grass" terrain=",1,,1">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="151" type="Grass" terrain="1,1,1,1">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="152" type="Grass" terrain="1,,1,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="153" type="Grass" terrain="1,,1,1">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="154" type="Grass" terrain=",1,1,1">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="155" type="Dirt" terrain=",2,,2">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="156" type="Dirt" terrain="2,2,2,2">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="157" type="Dirt" terrain="2,,2,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="158" type="Dirt" terrain="2,,2,2">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="159" type="Dirt" terrain=",2,2,2">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="160" type="Farm" terrain=",3,,3">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="161" type="Farm" terrain="3,3,3,3">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="162" type="Farm" terrain="3,,3,">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="163" type="Farm" terrain="3,,3,3">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="164" type="Farm" terrain=",3,3,3">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="165" type="Grass" terrain=",1,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="166" type="Grass" terrain="1,1,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="167" type="Grass" terrain="1,,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="168" type="Grass">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="169" type="Grass">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="170" type="Dirt" terrain=",2,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="171" type="Dirt" terrain="2,2,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="172" type="Dirt" terrain="2,,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="173" type="Dirt">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="174" type="Dirt">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="175" type="Farm" terrain=",3,,">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="176" type="Farm" terrain="3,3,,">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="177" type="Farm" terrain="3,,,">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="178" type="Farm">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="179" type="Farm">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="180" type="Stone" terrain=",,,7">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="181" type="Stone" terrain=",,7,7">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="182" type="Stone" terrain=",,7,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="183" type="Stone" terrain="7,7,7,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="184" type="Stone" terrain="7,7,,7">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="185" type="Sand" terrain=",,,4">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="186" type="Sand" terrain=",,4,4">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="187" type="Sand" terrain=",,4,">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="188" type="Sand" terrain="4,4,4,">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="189" type="Sand" terrain="4,4,,4">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="190" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="191" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="192" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="193" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="194" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="195" type="Stone" terrain=",7,,7">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="196" type="Stone" terrain="7,7,7,7">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="197" type="Stone" terrain="7,,7,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="198" type="Stone" terrain="7,,7,7">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="199" type="Stone" terrain=",7,7,7">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="200" type="Sand" terrain=",4,,4">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="201" type="Sand" terrain="4,4,4,4">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="202" type="Sand" terrain="4,,4,">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="203" type="Sand" terrain="4,,4,4">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="204" type="Sand" terrain=",4,4,4">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="205" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="206" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="207" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="208" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="209" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="210" type="Stone" terrain=",7,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="211" type="Stone" terrain="7,7,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="212" type="Stone" terrain="7,,,">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="213" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="214" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="215" type="Sand" terrain=",4,,">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="216" type="Sand" terrain="4,4,,">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="217" type="Sand" terrain="4,,,">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="218" type="Sand">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="219" type="Sand">
  <properties>
   <property name="cost" type="int" value="4"/>
  </properties>
 </tile>
 <tile id="220" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="221" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="222" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="223" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="224" type="Dirt">
  <properties>
   <property name="cost" type="int" value="2"/>
  </properties>
 </tile>
 <tile id="225" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="226" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="227" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="228" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="229" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="230" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="231" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="232" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="233" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="234" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="235" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="236" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="237" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="238" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="239" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="240" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="241" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="242" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="243" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="244" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="245" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="246" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="247" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="248" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="249" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="250" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="251" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="252" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="253" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="254" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="255" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="256" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="257" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="258" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="259" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="260" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="261" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="262" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="263" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="264" type="Stone">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="265" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="266" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="267" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="268" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="269" type="Road">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="270" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="271" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="272" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="273" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="274" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="275" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="276" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="277" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="278" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="279" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="280" type="Swamp" terrain=",,,9">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="281" type="Swamp" terrain=",,9,9">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="282" type="Swamp" terrain=",,9,">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="283" type="Swamp" terrain="9,9,9,">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="284" type="Swamp" terrain="9,9,,9">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="285" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="286" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="287" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="288" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="289" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="290" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="291" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="292" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="293" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="294" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="295" type="Swamp" terrain=",9,,9">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="296" type="Swamp" terrain="9,9,9,9">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="297" type="Swamp" terrain="9,,9,">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="298" type="Swamp" terrain="9,,9,9">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="299" type="Swamp" terrain=",9,9,9">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="300" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="301" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="302" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="303" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="304" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="305" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="306" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="307" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="308" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="309" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="310" type="Swamp" terrain=",9,,">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="311" type="Swamp" terrain="9,9,,">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="312" type="Swamp" terrain="9,,,">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="313">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="314">
  <properties>
   <property name="cost" type="int" value="30"/>
  </properties>
 </tile>
 <tile id="315" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="316" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="317" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="318" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="319" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="320" type="Wall" terrain=",,,8">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="32.1898" y="32.1898">
    <polygon points="0,0 0,-14.772 -6.39386,-13.6696 -8.15769,-9.92151 -12.3468,-3.30717 -12.5672,-0.220478"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="321" type="Wall" terrain=",,8,8">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="17.8587">
    <polygon points="0,0 31.7488,0 31.9693,14.5515 0,14.1106"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="322" type="Wall" terrain=",,8,">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="323" type="Wall" terrain="8,8,8,">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="31.9693" y="0.220478">
    <polygon points="0,0 0.220478,16.7563 -4.40956,18.5202 -6.61434,22.7092 -11.0239,25.355 -15.4335,24.4731 -20.0635,25.5754 -21.1659,29.3236 -22.4888,31.5284 -32.1898,31.9693 -32.4103,0"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="324" type="Wall" terrain="8,8,,8">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="0.220478">
    <polygon points="0,0 31.9693,0 31.9693,31.7488 20.0635,31.5284 0.220478,19.1816"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="325">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="326">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="327">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="328">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="329">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="330" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="331" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="332" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="333" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="334" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="335" type="Wall" terrain=",8,,8">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="31.3079" y="0.220478">
    <polygon points="0,0 -12.7877,-0.440956 -14.772,0.661434 -14.9925,5.51195 -15.4335,28.8826 -14.9925,30.8669 -14.5515,31.7488 0.440956,31.7488"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="336" type="Wall" terrain="8,8,8,8">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="2" x="-8.88178e-16" y="0.440956" width="31.9693" height="30.8669"/>
  </objectgroup>
 </tile>
 <tile id="337" type="Wall" terrain="8,,8,">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="0.220478" width="15.6539" height="31.3079"/>
  </objectgroup>
 </tile>
 <tile id="338" type="Wall" terrain="8,,8,8">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="0.440956">
    <polygon points="0,0 -0.220478,31.5284 32.1898,31.5284 32.1898,17.8587 16.0949,8.59864 13.2287,5.73243 15.6539,1.32287 15.6539,0.661434"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="339" type="Wall" terrain=",8,8,8">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="18.0792" y="-0.220478">
    <polygon points="0,0 13.8901,0.440956 13.4492,32.1898 -18.0792,32.1898 -18.0792,18.5202 -4.40956,11.9058"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="340">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="341">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="342">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="343">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="344">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="345" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="346" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="347" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="348" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="349" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="350" type="Wall" terrain=",8,,">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="15.4335" y="-0.440956">
    <polygon points="0,0 0.440956,12.7877 10.5829,14.5515 16.5358,12.3468 16.3154,0.661434"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="351" type="Wall" terrain="8,8,,">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="0.661434" y="0.440956" width="30.6464" height="14.9925"/>
  </objectgroup>
 </tile>
 <tile id="352" type="Wall" terrain="8,,,">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
  <objectgroup draworder="index" id="2">
   <object id="1" x="-0.440956" y="0">
    <polygon points="0,0 16.7563,-0.220478 1.10239,16.3154"/>
   </object>
  </objectgroup>
 </tile>
 <tile id="353" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="354" type="Wall">
  <properties>
   <property name="cost" type="int" value="255"/>
  </properties>
 </tile>
 <tile id="355">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="356">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="357">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="358">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
 <tile id="359">
  <properties>
   <property name="cost" type="int" value="1"/>
  </properties>
 </tile>
</tileset>
