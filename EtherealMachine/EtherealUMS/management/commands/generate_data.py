import random
import time
from django.core.management.base import BaseCommand
from EtherealUMS.models import Machine, Axis

class Command(BaseCommand):
    help = 'Generate machine and axis data'

    def handle(self, *args, **kwargs):
        machines = []

        # Create 20 machines
        for i in range(20):
            machine_id = f"81258856_{i}"
            machine_name = f"EMXP{i + 1}"
            tool_capacity = 24
            tool_offset = random.uniform(5, 40)
            feedrate = random.randint(10000, 20000)
            tool_in_use = random.randint(1, tool_capacity)

            machine = Machine.objects.create(
                machine_id=machine_id,
                machine_name=machine_name,
                tool_capacity=tool_capacity,
                tool_offset=tool_offset,
                feedrate=feedrate,
                tool_in_use=tool_in_use,
            )
            machines.append(machine)

            # Create 5 axes for each machine
            for axis_name in ['X', 'Y', 'Z', 'A', 'C']:
                max_acceleration = 200
                max_velocity = 60
                actual_position = random.uniform(-190, 190)
                target_position = random.uniform(-190, 191)
                distance_to_go = target_position - actual_position
                homed = random.choice([0, 1])
                acceleration = random.uniform(0, 150)
                velocity = random.uniform(0, 80)

                Axis.objects.create(
                    axis_name=axis_name,
                    max_acceleration=max_acceleration,
                    max_velocity=max_velocity,
                    actual_position=actual_position,
                    target_position=target_position,
                    distance_to_go=distance_to_go,
                    homed=homed,
                    acceleration=acceleration,
                    velocity=velocity,
                    machine=machine
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated machine and axis data.'))
