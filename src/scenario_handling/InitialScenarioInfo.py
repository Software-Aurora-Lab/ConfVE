from os import listdir
from cyber_record.record import Record
from config import AV_TESTING_APPROACH
from objectives.violation_number.oracles import RecordAnalyzer
from modules.perception.proto.perception_obstacle_pb2 import PerceptionObstacle
from modules.common.proto.geometry_pb2 import Point3D
from modules.perception.proto.traffic_light_detection_pb2 import TrafficLight


class InitialScenarioInfo:
    def __init__(self, is_record_file):
        self.is_record_file = is_record_file

    def update_generated_info(self, obs_group_path_list, adc_routing_list):
        self.obs_group_path_list = obs_group_path_list
        self.adc_routing_list = adc_routing_list
        self.count = len(obs_group_path_list)

    def update_record_path(self, scenario_record_dir_path):
        scenario_recordname_list = listdir(scenario_record_dir_path)
        scenario_recordname_list.sort()
        scenario_record_file_list = [f"{scenario_record_dir_path}/{recordname}" for recordname in
                                     scenario_recordname_list]

        self.scenario_record_file_list = scenario_record_file_list
        self.count = len(scenario_record_file_list)

    def update_violation_by_measuring(self):
        violation_num_list = []
        violation_results_list = []
        for i in self.scenario_record_file_list:
            ra = RecordAnalyzer(i)
            results = ra.analyze()
            violation_results_list.append(results)
            violation_num_list.append(len(results))
            print((f"id:{i}", f"Vio Count:{len(results)}", results))
        print(violation_num_list)
        self.violation_results_list = violation_results_list
        self.violation_num_list = violation_num_list

    def update_violation_directly(self, violation_results_list):
        self.violation_results_list = violation_results_list
        violation_num_list = [len(vr) for vr in violation_results_list]
        print(violation_results_list)
        print(violation_num_list)
        self.violation_num_list = violation_num_list

    def update(self, violation_results_list):
        # self.update_record_path(scenario_record_dir_path)
        self.update_violation_directly(violation_results_list)
        return self

    def extract_record_info(self):
        obs_perception_list = []
        routing_request_list = []
        traffic_lights_list = []
        for scenario_record_file_path in self.scenario_record_file_list:
            record = Record(scenario_record_file_path)
            obs_temp_list = []
            traffic_temp_list = []
            for topic, message, t in record.read_messages():
                if topic == "/apollo/perception/obstacles":
                    perception_obstacles = list(message.perception_obstacle)
                    obs_instance_list = [self.obs_instance(perception_obstacle) for perception_obstacle in
                                         perception_obstacles]
                    obs_temp_list.append(obs_instance_list)
                elif topic == "/apollo/routing_response":
                    if AV_TESTING_APPROACH == "scenoRITA":
                        routing_message_module_name = "routing routing..."
                    elif AV_TESTING_APPROACH == "DoppelTest":
                        routing_message_module_name = "MAGGIE"
                    else:
                        routing_message_module_name = ""
                    if message.routing_request.header.module_name == routing_message_module_name:
                        routing_request = message.routing_request
                        routing_request_list.append(routing_request)
                elif topic == "/apollo/perception/traffic_light":
                    traffic_lights = list(message.traffic_light)
                    traffic_instance_list = [self.traffic_instance(traffic_light) for traffic_light in traffic_lights]
                    traffic_temp_list.append(traffic_instance_list)

            obs_perception_list.append(obs_temp_list)
            traffic_lights_list.append(traffic_temp_list)

            self.obs_perception_list = obs_perception_list
            self.routing_request_list = routing_request_list
            self.traffic_lights_list = traffic_lights_list

    def obs_instance(self, perception_obstacle):
        points = []
        for pp in list(perception_obstacle.polygon_point):
            p = Point3D(x=pp.x, y=pp.y, z=pp.z)
            points.append(p)

        obs = PerceptionObstacle(
            id=perception_obstacle.id,
            position=Point3D(x=perception_obstacle.position.x, y=perception_obstacle.position.y,
                             z=perception_obstacle.position.z),
            theta=perception_obstacle.theta,
            velocity=Point3D(x=perception_obstacle.velocity.x, y=perception_obstacle.velocity.y,
                             z=perception_obstacle.velocity.z),
            acceleration=Point3D(x=perception_obstacle.acceleration.x, y=perception_obstacle.acceleration.y,
                                 z=perception_obstacle.acceleration.z),
            length=perception_obstacle.length,
            width=perception_obstacle.width,
            height=perception_obstacle.height,
            type=perception_obstacle.type,
            timestamp=perception_obstacle.timestamp,
            tracking_time=perception_obstacle.tracking_time,
            polygon_point=points
        )

        return obs

    def traffic_instance(self, traffic_light):
        tl = TrafficLight(
            color=traffic_light.color,
            id=traffic_light.id,
            confidence=traffic_light.confidence
        )
        return tl