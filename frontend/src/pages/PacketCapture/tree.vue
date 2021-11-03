<template>
  <div class="q-pa-sm">a</div>
</template>

<script>
import { onMounted, ref } from "vue";
import axios from "axios";
export default {
  setup() {
    const fetchPackets = async () => {
      //   let { data } = await axios.get(
      //     "http://192.168.169.128:5000/networkdata/pcap?filename=ca89bba5-268f-459e-b44a-d18fb28af141.pcap"
      //   );
      //   let frame_info = data[0].packet_data.frame_info
      //   let layers = data[0].packet_data.layers;
      //   console.log(layers);
      //   let l1 = layers[0];
      //   Object.entries(l1).forEach(([key, value]) => {
      //     console.log({});
      //   });
      //   const packet_data = data.packet_data;
      //   console.log(packet_data);
      //   let frame_info = packet_data.frame_info;
      //   console.log(frame_info);
      //   packet_data.map((d) => {
      //     return {
      //       label: "Frame",
      //       children: [
      //         {
      //           label: `Frame Packet Length: ${d.frame_info._all_fields.frame.cap_len}`,
      //         },
      //         {
      //           label: `Frame Number: ${d.frame_info._all_fields.frame.number}`,
      //         },
      //         {
      //           label: `Frame Offset Shift: ${d.frame_info._all_fields.frame.offset_shift}`,
      //         },
      //         {
      //           label: `Frame Protocols: ${d.frame_info._all_fields.frame.protocols}`,
      //         },
      //         {
      //           label: `Frame Time: ${d.frame_info._all_fields.frame.time}`,
      //         },
      //         {
      //           label: `Frame Time Delta: ${d.frame_info._all_fields.frame.time_delta}`,
      //         },
      //         {
      //           label: `Frame Time Epoch: ${d.frame_info._all_fields.frame.time_epoch}`,
      //         },
      //       ],
      //       label: "Ethernet",
      //       children: [
      //         {
      //           label: `Destination: ${d.layers[0]._all_fields.eth.dst}`,
      //         },
      //         {
      //           label: `Destination Raw: ${d.layers[0]._all_fields.eth.dst_raw}`,
      //         },
      //         {
      //           label: `Ethernet Destination Tree`,
      //           children: [
      //             {
      //               label: `Ethernet Address: ${d.layers[0]._all_fields.eth.dst_tree.eth.addr}`,
      //             },
      //             {
      //               label: `Ethernet Address OUI: ${d.layers[0]._all_fields.eth.dst_tree.eth.addr.oui}`,
      //             },
      //             {
      //               label: `Ethernet Address OUI RAW: ${d.layers[0]._all_fields.eth.dst_tree.eth.addr.oui_raw}`,
      //             },
      //             {
      //               label: `Ethernet Address OUI Resolved: ${d.layers[0]._all_fields.eth.dst_tree.eth.addr.oui_resolved}`,
      //             },
      //             {
      //               label: `Ethernet Address OUI Resolved Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.addr.oui_resolved_raw}`,
      //             },
      //             {
      //               label: `Ethernet Address Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.addr_raw}`,
      //             },
      //             {
      //               label: `Ethernet Address Resolved: ${d.layers[0]._all_fields.eth.dst_tree.eth.addr_resolved}`,
      //             },
      //             {
      //               label: `Ethernet Address Resolved Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.addr_resolved_raw}`,
      //             },
      //             {
      //               label: `Ethernet Destination IG BIT: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst.ig}`,
      //             },
      //             {
      //               label: `Ethernet Destination IG BIT Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst.ig_raw}`,
      //             },
      //             {
      //               label: `Ethernet Destination LG BIT: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst.lg}`,
      //             },
      //             {
      //               label: `Ethernet Destination LG BIT Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst.lg_raw}`,
      //             },
      //             {
      //               label: `Ethernet Destination OUI: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst.oui}`,
      //             },
      //             {
      //               label: `Ethernet Destination OUI Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst.oui_raw}`,
      //             },
      //             {
      //               label: `Ethernet Destination OUI Resolved: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst.oui_resolved}`,
      //             },
      //             {
      //               label: `Ethernet Destination OUI Resolved Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst.oui_resolved_raw}`,
      //             },
      //             {
      //               label: `Ethernet Destination Resolved: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst_resolved}`,
      //             },
      //             {
      //               label: `Ethernet Destination Resolved Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.dst_resolved_raw}`,
      //             },
      //             {
      //               label: `Ethernet IG: ${d.layers[0]._all_fields.eth.dst_tree.eth.ig}`,
      //             },
      //             {
      //               label: `Ethernet IG Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.ig_raw}`,
      //             },
      //             {
      //               label: `Ethernet LG: ${d.layers[0]._all_fields.eth.dst_tree.eth.lg}`,
      //             },
      //             {
      //               label: `Ethernet LG Raw: ${d.layers[0]._all_fields.eth.dst_tree.eth.lg_raw}`,
      //             },
      //           ],
      //         },
      //         {
      //           label: `Ethernet Source: ${d.layers[0]._all_fields.eth.src}`,
      //         },
      //         {
      //           label: `Ethernet Source Raw: ${d.layers[0]._all_fields.eth.src_raw}`,
      //         },
      //         {
      //           label: "Ethernet Source Tree",
      //           children: [
      //             {
      //               label: `Ethernet Address: ${d.layers[0]._all_fields.eth.src_tree.eth.addr}`,
      //             },
      //             {
      //               label: `Ethernet Address OUI: ${d.layers[0]._all_fields.eth.src_tree.eth.addr.oui}`,
      //             },
      //             {
      //               label: `Ethernet Address OUI RAW: ${d.layers[0]._all_fields.eth.src_tree.eth.addr.oui_raw}`,
      //             },
      //             {
      //               label: `Ethernet Address OUI Resolved: ${d.layers[0]._all_fields.eth.src_tree.eth.addr.oui_resolved}`,
      //             },
      //             {
      //               label: `Ethernet Address OUI Resolved Raw: ${d.layers[0]._all_fields.eth.src_tree.eth.addr.oui_resolved_raw}`,
      //             },
      //             {
      //               label: `Ethernet Address Raw: ${d.layers[0]._all_fields.eth.src_tree.eth.addr_raw}`,
      //             },
      //             {
      //               label: `Ethernet Address Resolved: ${d.layers[0]._all_fields.eth.src_tree.eth.addr_resolved}`,
      //             },
      //             {
      //               label: `Ethernet Address Resolved Raw: ${d.layers[0]._all_fields.eth.src_tree.eth.addr_resolved_raw}`,
      //             },
      //             {
      //               label: `Ethernet Source IG BIT: ${d.layers[0]._all_fields.eth.src_tree.eth.src.ig}`,
      //             },
      //             {
      //               label: `Ethernet Source IG BIT Raw: ${d.layers[0]._all_fields.eth.src_tree.eth.src.ig_raw}`,
      //             },
      //             {
      //               label: `Ethernet Source LG BIT: ${d.layers[0]._all_fields.eth.src_tree.eth.src.lg}`,
      //             },
      //             {
      //               label: `Ethernet Source LG BIT Raw: ${d.layers[0]._all_fields.eth.src_tree.eth.src.lg_raw}`,
      //             },
      //             {
      //               label: `Ethernet Source OUI: ${d.layers[0]._all_fields.eth.src_tree.eth.src.oui}`,
      //             },
      //             {
      //               label: `Ethernet Source OUI Raw: ${d.layers[0]._all_fields.eth.src_tree.eth.src.oui_raw}`,
      //             },
      //             {
      //               label: `Ethernet Source OUI Resolved: ${d.layers[0]._all_fields.eth.src_tree.eth.src.oui_resolved}`,
      //             },
      //             {
      //               label: `Ethernet Source OUI Resolved Raw: ${d.layers[0]._all_fields.eth.src_tree.eth.src.oui_resolved_raw}`,
      //             },
      //             {
      //               label: `Ethernet Source Resolved: ${d.layers[0]._all_fields.eth.src_tree.eth.src_resolved}`,
      //             },
      //             {
      //               label: `Ethernet Source Resolved Raw: ${d.layers[0]._all_fields.eth.src_tree.eth.src_resolved_raw}`,
      //             },
      //           ],
      //         },
      //       ],
      //       label: `IP Address`,
      //       children: [
      //         {
      //           label: `IP Address ${d.layers[1]._all_fields.ip.addr}`,
      //         },
      //         {
      //           label: `IP Address Raw`,
      //           children: [
      //             {
      //               label: d.layers[1]._all_fields.ip.addr_raw[0],
      //             },
      //             {
      //               label: d.layers[1]._all_fields.ip.addr_raw[1],
      //             },
      //           ],
      //         },
      //         {
      //           label: `IP Checksum ${d.layers[1]._all_fields.ip.checksum}`,
      //         },
      //         {
      //           label: `IP Checksum Status ${d.layers[1]._all_fields.ip.checksum_status}`,
      //         },
      //         {
      //           label: `IP Checksum Raw ${d.layers[1]._all_fields.ip.checksum_raw}`,
      //         },
      //         {
      //           label: `IP DS Field ${d.layers[1]._all_fields.ip.dsfield}`,
      //         },
      //         {
      //           label: `IP DS Field Raw ${d.layers[1]._all_fields.ip.dsfield_raw}`,
      //         },
      //         {
      //           label: `IP DS Field Full (DSCP: ${d.layers[1]._all_fields.ip.dsfield_tree.ip.dsfield.dscp}, ECN: ${d.layers[1]._all_fields.ip.dsfield_tree.ip.dsfield.ecn})`,
      //         },
      //         {
      //           label: `IP Destination ${d.layers[1]._all_fields.ip.dsfield_tree.ip.dst}`,
      //         },
      //         {
      //           label: `IP Destination Host ${d.layers[1]._all_fields.ip.dsfield_tree.ip.dst_host}`,
      //         },
      //         {
      //           label: `IP Destination Host Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.dst_host_raw}`,
      //         },
      //         {
      //           label: `IP Destination Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.dst_raw}`,
      //         },
      //         {
      //           label: `IP Flags ${d.layers[1]._all_fields.ip.dsfield_tree.ip.flags}`,
      //         },
      //         {
      //           label: `IP Flags Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.flags_rag}`,
      //         },
      //         {
      //           label: `IP Flags Tree`,
      //           children: [
      //             {
      //               label: `IP Flags DF ${d.layers[1]._all_fields.ip.dsfield_tree.ip.flags_tree.df}`,
      //             },
      //             {
      //               label: `IP Flags DF Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.flags_tree.df_raw}`,
      //             },
      //             {
      //               label: `IP Flags MF ${d.layers[1]._all_fields.ip.dsfield_tree.ip.flags_tree.mf}`,
      //             },
      //             {
      //               label: `IP Flags MF Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.flags_tree.mf_raw}`,
      //             },
      //             {
      //               label: `IP Flags RB  ${d.layers[1]._all_fields.ip.dsfield_tree.ip.flags_tree.rb}`,
      //             },
      //             {
      //               label: `IP Flags RB Raw  ${d.layers[1]._all_fields.ip.dsfield_tree.ip.flags_tree.rb_raw}`,
      //             },
      //           ],
      //         },
      //         {
      //           label: `IP Frag OffSet ${d.layers[1]._all_fields.ip.dsfield_tree.ip.frag_offset}`,
      //         },
      //         {
      //           label: `IP Frag OffSet Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.frag_offset_raw}`,
      //         },
      //         {
      //           label: `IP Frag HDR Len ${d.layers[1]._all_fields.ip.dsfield_tree.ip.hdr_len}`,
      //         },
      //         {
      //           label: `IP Frag HDR Len Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.hdr_len_raw}`,
      //         },
      //         {
      //           label: `IP Host ${d.layers[1]._all_fields.ip.dsfield_tree.ip.host}`,
      //         },
      //         {
      //           label: `IP Host Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.host_raw}`,
      //         },
      //         {
      //           label: `IP ID ${d.layers[1]._all_fields.ip.dsfield_tree.ip.id}`,
      //         },
      //         {
      //           label: `IP Len ${d.layers[1]._all_fields.ip.dsfield_tree.ip.len}`,
      //         },
      //         {
      //           label: `IP Len Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.len_raw}`,
      //         },
      //         {
      //           label: `IP Proto ${d.layers[1]._all_fields.ip.dsfield_tree.ip.proto}`,
      //         },
      //         {
      //           label: `IP Proto Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.proto_raw}`,
      //         },
      //         {
      //           label: `IP Source  ${d.layers[1]._all_fields.ip.dsfield_tree.ip.src}`,
      //         },
      //         {
      //           label: `IP Source Host  ${d.layers[1]._all_fields.ip.dsfield_tree.ip.src_host}`,
      //         },
      //         {
      //           label: `IP Source Host Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.src_host_raw}`,
      //         },
      //         {
      //           label: `IP Source Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.src_raw}`,
      //         },
      //         {
      //           label: `IP Time to Live ${d.layers[1]._all_fields.ip.dsfield_tree.ip.ttl}`,
      //         },
      //         {
      //           label: `IP Time to Live Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.ttl_raw}`,
      //         },
      //         {
      //           label: `IP Version ${d.layers[1]._all_fields.ip.dsfield_tree.ip.version}`,
      //         },
      //         {
      //           label: `IP Version Raw ${d.layers[1]._all_fields.ip.dsfield_tree.ip.version_raw}`,
      //         },
      //       ],
      //     };
      //   });
    };

    onMounted(() => {
      fetchPackets();
      // fetchData();
      //   fetchPCAPS();
    });
  },
};
</script>
