# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Wrapper for the lookback RNN model."""

# internal imports
from magenta.models.lookback_rnn import lookback_rnn_generator
from magenta.models.shared import melody_rnn_model


class LookbackRnnModel(melody_rnn_model.MelodyRnnModel):
  """Lookback RNN model class."""

  def _create_generator_fn(self):
    return lookback_rnn_generator.create_generator
